from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, Set, Tuple, Union

import grpc
from buildgrid_metering.client import SyncMeteringServiceClient
from grpc import Compression

from buildgrid.server.actioncache.caches.action_cache_abc import ActionCacheABC
from buildgrid.server.auth.config import parse_auth_config
from buildgrid.server.auth.enums import AuthMetadataAlgorithm, AuthMetadataMethod
from buildgrid.server.auth.manager import AuthManager, HeadersAuthManager, JWTAuthManager
from buildgrid.server.cas.storage.index.index_abc import IndexABC
from buildgrid.server.cas.storage.storage_abc import StorageABC
from buildgrid.server.client.asset import AssetClient
from buildgrid.server.monitoring import MonitoringBus, MonitoringOutputFormat, MonitoringOutputType, StatsDTagFormat
from buildgrid.server.scheduler import Scheduler
from buildgrid.server.servicer import Instance
from buildgrid.server.settings import DEFAULT_JWKS_REFETCH_INTERVAL_MINUTES
from buildgrid.server.sql.provider import SqlProvider

from .mapper import map_key

if TYPE_CHECKING:
    from buildgrid.server.redis.provider import RedisProvider


@dataclass
class ChannelConfig:
    insecure_mode: bool
    address: str
    credentials: Optional[Dict[str, str]] = None


@dataclass
class InstanceConfig:
    name: str
    description: Optional[str]
    connections: List[Union[SqlProvider, "RedisProvider"]]
    storages: List[StorageABC]
    caches: List[ActionCacheABC]
    clients: List[Union[SyncMeteringServiceClient, AssetClient]]
    schedulers: List[Scheduler]
    services: List[Union[Instance]]


@dataclass
class CleanupConfig:
    name: str
    index: IndexABC


@dataclass
class BuildgridConfig:
    description: Optional[str]
    authorization: Optional[AuthManager]
    monitoring: Optional[MonitoringBus]
    thread_pool_size: Optional[int]
    server_reflection: bool
    grpc_compression: grpc.Compression
    server: List[ChannelConfig]
    grpc_server_options: Optional[Sequence[Tuple[str, Any]]]
    connections: List[Union[SqlProvider, "RedisProvider"]]
    storages: List[StorageABC]
    caches: List[ActionCacheABC]
    clients: List[Union[SyncMeteringServiceClient, AssetClient]]
    schedulers: List[Union[SyncMeteringServiceClient, AssetClient]]
    instances: List[InstanceConfig]
    cleanup: List[CleanupConfig]


def populate_authorization_config(conf: Dict[str, Any]) -> Optional[AuthManager]:
    method = map_key(conf, "method", decoder=AuthMetadataMethod)
    acl_config = map_key(conf, "acl-config", decoder=parse_auth_config, default=None)
    allow_unauthorized_instances: Set[str] = set(map_key(conf, "allow-unauthorized-instances", default=[]))

    def load_secret(file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    if method == AuthMetadataMethod.JWT:
        return JWTAuthManager(
            secret=map_key(conf, "secret", decoder=load_secret, default=None),
            algorithm=map_key(
                conf, "algorithm", decoder=AuthMetadataAlgorithm, default=AuthMetadataAlgorithm.UNSPECIFIED
            ),
            jwks_urls=map_key(conf, "jwks-url", decoder=normalize_str_or_list_strs, default=None),
            audiences=map_key(conf, "audience", decoder=normalize_str_or_list_strs, default=None),
            jwks_fetch_minutes=map_key(conf, "jwks-fetch-minutes", default=DEFAULT_JWKS_REFETCH_INTERVAL_MINUTES),
            acls=acl_config,
            allow_unauthorized_instances=allow_unauthorized_instances,
        )

    if method == AuthMetadataMethod.HEADERS:
        return HeadersAuthManager(
            acls=acl_config,
            allow_unauthorized_instances=allow_unauthorized_instances,
        )

    return None


def populate_monitoring_config(conf: Dict[str, Any]) -> Optional[MonitoringBus]:
    def parse_metric_prefix(value: str) -> str:
        return value.strip().rstrip(".") + "."

    if not map_key(conf, "enabled", default=True):
        return None

    return MonitoringBus(
        endpoint_type=map_key(
            conf, "endpoint-type", decoder=MonitoringOutputType, default=MonitoringOutputType.STDOUT
        ),
        endpoint_location=map_key(conf, "endpoint-location", default=None),
        metric_prefix=map_key(conf, "metric-prefix", decoder=parse_metric_prefix, default=""),
        serialisation_format=map_key(
            conf, "serialization-format", decoder=MonitoringOutputFormat, default=MonitoringOutputFormat.STATSD
        ),
        tag_format=map_key(conf, "tag-format", decoder=StatsDTagFormat, default=StatsDTagFormat.INFLUX_STATSD),
        additional_tags=map_key(conf, "additional-tags", default=None),
    )


def populate_instance_config(confs: List[Dict[str, Any]]) -> List[InstanceConfig]:
    return [
        InstanceConfig(
            name=map_key(conf, "name"),
            description=map_key(conf, "description", default=None),
            connections=map_key(conf, "connections", default=[]),
            storages=map_key(conf, "storages", default=[]),
            caches=map_key(conf, "caches", default=[]),
            clients=map_key(conf, "clients", default=[]),
            schedulers=map_key(conf, "schedulers", default=[]),
            services=map_key(conf, "services"),
        )
        for conf in confs
    ]


def populate_cleanup_config(confs: List[Dict[str, Any]]) -> List[CleanupConfig]:
    return [
        CleanupConfig(
            name=map_key(conf, "instance-name"),
            index=map_key(conf, "index"),
        )
        for conf in confs
    ]


def populate_buildgrid_config(conf: Dict[str, Any]) -> BuildgridConfig:
    return BuildgridConfig(
        description=map_key(conf, "description", default=""),
        authorization=map_key(conf, "authorization", decoder=populate_authorization_config, default=None),
        monitoring=map_key(conf, "monitoring", decoder=populate_monitoring_config, default=None),
        thread_pool_size=map_key(conf, "thread-pool-size", default=None),
        grpc_compression=map_key(
            conf, "grpc-compression", decoder=parse_compression, default=Compression.NoCompression
        ),
        server_reflection=map_key(conf, "server-reflection", default=True),
        grpc_server_options=map_key(conf, "grpc-server-options", decoder=lambda v: tuple(v.items()), default=None),
        server=map_key(conf, "server", default=[]),
        connections=map_key(conf, "connections", default=[]),
        storages=map_key(conf, "storages", default=[]),
        caches=map_key(conf, "caches", default=[]),
        clients=map_key(conf, "clients", default=[]),
        schedulers=map_key(conf, "schedulers", default=[]),
        instances=map_key(conf, "instances", decoder=populate_instance_config, default=[]),
        cleanup=map_key(conf, "cleanup", decoder=populate_cleanup_config, default=[]),
    )


def parse_compression(conf: str) -> Compression:
    if conf == "NoCompression":
        return Compression.NoCompression
    elif conf == "Deflate":
        return Compression.Deflate
    elif conf == "Gzip":
        return Compression.Gzip
    else:
        raise ValueError(f"Unsupported grpc-compression {conf} specified")


def normalize_str_or_list_strs(conf: Union[str, List[str]]) -> List[str]:
    """Normalize some configs that are allowed to be either a singleton or a list to a list"""
    if isinstance(conf, str):
        return [conf]
    return conf
