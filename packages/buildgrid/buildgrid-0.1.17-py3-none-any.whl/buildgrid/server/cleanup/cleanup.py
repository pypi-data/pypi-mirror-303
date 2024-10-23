# Copyright (C) 2020 Bloomberg LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import threading
import time
from contextlib import ExitStack
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import Digest
from buildgrid.server.cas.storage.index.index_abc import IndexABC
from buildgrid.server.context import instance_context
from buildgrid.server.logging import buildgrid_logger
from buildgrid.server.metrics_names import METRIC
from buildgrid.server.metrics_utils import publish_counter_metric, publish_gauge_metric, timer
from buildgrid.server.monitoring import get_monitoring_bus
from buildgrid.server.threading import ContextThreadPoolExecutor, ContextWorker

LOGGER = buildgrid_logger(__name__)


def _digests_str(digests: List[Digest]) -> str:
    return f"{len(digests)} digests ({sum(d.size_bytes for d in digests)} bytes)"


class CASCleanUp:
    """Creates a CAS cleanup service."""

    def __init__(
        self,
        dry_run: bool,
        high_watermark: int,
        low_watermark: int,
        sleep_interval: int,
        batch_size: int,
        only_if_unused_for: timedelta,
        indexes: Dict[str, IndexABC],
        monitor: bool,
    ) -> None:
        self._stack = ExitStack()
        self._dry_run = dry_run

        self._high_watermark = high_watermark
        self._low_watermark = low_watermark
        self._batch_size = batch_size
        self._only_if_unused_for = only_if_unused_for

        self._indexes = indexes

        self._is_instrumented = monitor

        self._sleep_interval = sleep_interval

    # --- Public API ---

    def start(self, timeout: Optional[float] = None) -> None:
        """Start cleanup service"""
        if self._is_instrumented:
            self._stack.enter_context(get_monitoring_bus())
        worker = self._stack.enter_context(ContextWorker(self._begin_cleanup, "CleanUpLauncher"))
        worker.wait(timeout=timeout)

    def stop(self, *args: Any, **kwargs: Any) -> None:
        """Stops the cleanup service"""
        LOGGER.info("Stopping Cleanup Service.")
        self._stack.close()

    def _begin_cleanup(self, stop_requested: threading.Event) -> None:
        if self._dry_run:
            for instance_name in self._indexes.keys():
                self._calculate_cleanup(instance_name)
            return

        attempts = 0
        with ContextThreadPoolExecutor(max_workers=len(self._indexes)) as ex:
            while True:
                futures = {
                    instance_name: ex.submit(self._cleanup_worker, instance_name, stop_requested)
                    for instance_name in self._indexes.keys()
                }

                failed = False
                for instance_name, future in futures.items():
                    try:
                        future.result()
                        LOGGER.info("Cleanup completed.", tags=dict(instance_name=instance_name))
                    except Exception:
                        LOGGER.exception("Cleanup failed.", tags=dict(instance_name=instance_name))
                        failed = True

                if not failed:
                    break

                # Exponential backoff before retrying
                sleep_time = 1.6**attempts
                LOGGER.info("Retrying Cleanup after delay...", tags=dict(sleep_time_seconds=sleep_time))
                stop_requested.wait(timeout=sleep_time)
                attempts += 1
                continue

    def _calculate_cleanup(self, instance_name: str) -> None:
        """Work out which blobs will be deleted by the cleanup command."""
        with instance_context(instance_name):
            LOGGER.info("Cleanup dry run.", tags=dict(instance_name=instance_name))
            index = self._indexes[instance_name]
            only_delete_before = self._get_last_accessed_threshold()
            total_size = index.get_total_size()
            LOGGER.info(
                "Calculated CAS size.",
                tags=dict(
                    total_size=total_size,
                    high_watermark_bytes=self._high_watermark,
                    low_watermark_bytes=self._low_watermark,
                ),
            )
            if total_size >= self._high_watermark:
                required_space = total_size - self._low_watermark
                cleared_space = index.delete_n_bytes(
                    required_space, dry_run=True, protect_blobs_after=only_delete_before
                )
                LOGGER.info(f"Determined {cleared_space} of the requested {required_space} bytes would be deleted.")
            else:
                LOGGER.info(f"Total size {total_size} is less than the high water mark, " f"nothing will be deleted.")

    def _do_cleanup_batch(
        self,
        instance_name: str,
        index: IndexABC,
        only_delete_before: datetime,
        total_size: int,
        stop_requested: threading.Event,
    ) -> None:
        batch_start_time = time.time()

        LOGGER.info("Deleting bytes from the index.", tags=dict(batch_size=self._batch_size))
        bytes_deleted = index.delete_n_bytes(self._batch_size, protect_blobs_after=only_delete_before)

        if not bytes_deleted:
            err = (
                "Marked 0 digests for deletion, even though cleanup was triggered. "
                "This may be because the remaining digests have been accessed within "
                f"{only_delete_before}."
            )
            if total_size >= self._high_watermark:
                LOGGER.error(f"{err} Total size still remains greater than high watermark!")
            else:
                LOGGER.warning(err)
            stop_requested.wait(timeout=self._sleep_interval)  # Avoid a busy loop when we can't make progress
            return

        LOGGER.info("Bulk deleted bytes from index.", tags=dict(bytes_deleted=bytes_deleted))

        if self._is_instrumented:
            batch_duration = time.time() - batch_start_time
            bytes_deleted_per_second = bytes_deleted / batch_duration
            publish_gauge_metric(METRIC.CLEANUP.BYTES_DELETED_PER_SECOND, bytes_deleted_per_second)
            publish_counter_metric(METRIC.CLEANUP.BYTES_DELETED_COUNT, bytes_deleted)

    def _cleanup_worker(self, instance_name: str, stop_requested: threading.Event) -> None:
        """Cleanup when full"""
        with instance_context(instance_name):
            index = self._indexes[instance_name]
            LOGGER.info("Cleanup started.", tags=dict(instance_name=instance_name))

            while not stop_requested.is_set():
                # When first starting a loop, we will also include any remaining delete markers as part of
                # the total size.
                total_size = index.get_total_size()
                self.publish_total_size_metric(total_size)

                if total_size >= self._high_watermark:
                    to_delete = total_size - self._low_watermark
                    LOGGER.info(
                        "High watermark exceeded. Deleting items from storage/index.",
                        tags=dict(total_bytes=total_size, min_bytes_to_delete=to_delete, instance_name=instance_name),
                    )

                    with timer(METRIC.CLEANUP.DURATION):
                        while not stop_requested.is_set() and total_size > self._low_watermark:
                            only_delete_before = self._get_last_accessed_threshold()
                            with timer(METRIC.CLEANUP.BATCH_DURATION):
                                self._do_cleanup_batch(
                                    instance_name=instance_name,
                                    index=index,
                                    only_delete_before=only_delete_before,
                                    total_size=total_size,
                                    stop_requested=stop_requested,
                                )
                            total_size = index.get_total_size()
                            self.publish_total_size_metric(total_size)
                            LOGGER.info("Finished cleanup batch.", tags=dict(non_stale_total_bytes=total_size))

                    LOGGER.info("Finished cleanup.", tags=dict(total_bytes=total_size))

                stop_requested.wait(timeout=self._sleep_interval)

    def _get_last_accessed_threshold(self) -> datetime:
        return datetime.utcnow() - self._only_if_unused_for

    def publish_total_size_metric(self, total_size: int) -> None:
        if self._is_instrumented:
            publish_gauge_metric(METRIC.CLEANUP.TOTAL_BYTES_COUNT, total_size)
            publish_gauge_metric(METRIC.CLEANUP.LOW_WATERMARK_BYTES_COUNT, self._low_watermark)
            publish_gauge_metric(METRIC.CLEANUP.HIGH_WATERMARK_BYTES_COUNT, self._high_watermark)
