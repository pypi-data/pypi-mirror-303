KEY_REDIS = "redis"
KEY_REDIS_HOST = "host"
KEY_REDIS_PORT = "port"
KEY_REDIS_DB = "db"
KEY_REDIS_PASSWORD = "password"
KEY_REDIS_POOL_SIZE = "pool_size"
KEY_REDIS_DEFAULT_KEY = "default"
"""
redis configuration format
====
{
  "redis": {
    "default": {
      "host": "127.0.0.1",
      "port": 6379,
      "db": 0,
      "password": "",
      "pool_size": 1
    }
  }
}
"""
