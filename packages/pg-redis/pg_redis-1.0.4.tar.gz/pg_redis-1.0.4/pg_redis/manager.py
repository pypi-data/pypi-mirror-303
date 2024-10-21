from pg_common import SingletonBase, log_error, log_info
from pg_redis import RedisManager
import json


__all__ = ("GameConfigManager", )


GAME_CONFIG_REDIS_KEY = "__GAME_CONFIG__"


class _GameConfigManager(SingletonBase):
    def __init__(self):
        self._cfg: dict[str, dict] = {}

    async def reload(self):
        _r = await RedisManager.get_redis()
        if _r:
            _games = await _r.smembers(GAME_CONFIG_REDIS_KEY)
            for _g in _games:
                _json = await _r.get("%s:%s" % (GAME_CONFIG_REDIS_KEY, _g))
                if _json:
                    self._cfg[_g] = json.loads(_json)
                    log_info(f"===[{_g}]:[{self._cfg[_g]['version']}]===")

        else:
            log_error("!!!!!!!can not get redis client.")

    def get_config(self, game: str) -> dict:
        if game in self._cfg:
            return self._cfg[game]
        return None


GameConfigManager = _GameConfigManager()
