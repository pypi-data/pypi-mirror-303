from pg_common import SingletonBase, RuntimeException, log_warn
from pg_redis.define import *
from pg_environment import config
from redis import asyncio as redis


__all__ = ("RedisManager", )


class _RedisManager(SingletonBase):
    def __init__(self):
        self._redis_client = {}
        _cfg_redis = config.get_conf(KEY_REDIS)
        if not _cfg_redis:
            log_warn(f"redis config not defined.")
            return
        for _k, _v in _cfg_redis.items():
            _pool_cfg = redis.ConnectionPool(host=_v[KEY_REDIS_HOST], port=_v[KEY_REDIS_PORT],
                                             db=_v[KEY_REDIS_DB], password=_v[KEY_REDIS_PASSWORD],
                                             decode_responses=True, max_connections=_v[KEY_REDIS_POOL_SIZE])
            self._redis_client[_k] = redis.StrictRedis(connection_pool=_pool_cfg)

    def get_redis(self, svr_name=KEY_REDIS_DEFAULT_KEY):
        if svr_name in self._redis_client:
            return self._redis_client[svr_name]
        elif KEY_REDIS_DEFAULT_KEY in self._redis_client:
            return self._redis_client[KEY_REDIS_DEFAULT_KEY]
        else:
            raise RuntimeException("getRedisClient", f"Can't find redis config for {svr_name}")


RedisManager = _RedisManager()
