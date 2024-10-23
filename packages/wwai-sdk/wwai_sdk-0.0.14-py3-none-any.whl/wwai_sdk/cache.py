import logging
import os

logger = logging.getLogger(__name__)


class WwaiSdkCache:
    def __init__(self,
                 cache_type="local",
                 redis_host=None,
                 redis_port=6379,
                 redis_password=None,
                 redis_db=0
                 ):
        self.cache_type = cache_type
        self.cache_prefix = "wwai-sdk-cache"
        if cache_type == "redis":
            try:
                import redis
            except ImportError:
                raise ImportError("Please install redis with `pip install redis`")

            password = os.getenv("REDIS_PASSWORD", "") if os.getenv("REDIS_PASSWORD", "") != "" else redis_password
            if password is not None and (password.lower() == "none" or password.lower() == "null"):
                password = None
            self.redis = redis.StrictRedis(
                host=os.getenv("REDIS_HOST", redis_host),
                port=int(os.getenv("REDIS_PORT", redis_port)),
                db=int(os.getenv("REDIS_DB", redis_db)),
                password=password,
                decode_responses=True,
                socket_timeout=10,
                socket_connect_timeout=10,
                socket_keepalive=True,
            )
        else:
            try:
                from diskcache import Cache
                import tempfile
            except ImportError:
                raise ImportError("Please install diskcache with `pip install diskcache`")
            cache_dir = f"{tempfile.gettempdir()}/wwai-sdk-cache"
            self.cache = Cache(cache_dir)
            print(f"Cache dir: {cache_dir}")

    def get(self, key):
        if self.cache_type == "redis":
            return self.redis.get(f"{self.cache_prefix}:{key}")
        else:
            return self.cache.get(f"{self.cache_prefix}:{key}")

    def set(self, key, value, ttl=None):
        if self.cache_type == "redis":
            return self.redis.set(f"{self.cache_prefix}:{key}", value, ex=ttl)
        else:
            return self.cache.set(f"{self.cache_prefix}:{key}", value, expire=ttl)

    def delete(self, key):
        if self.cache_type == "redis":
            return self.redis.delete(f"{self.cache_prefix}:{key}")
        else:
            return self.cache.delete(f"{self.cache_prefix}:{key}")
