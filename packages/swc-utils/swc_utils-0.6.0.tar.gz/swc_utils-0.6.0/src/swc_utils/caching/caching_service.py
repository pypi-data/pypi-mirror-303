from .cache import Cache


class CachingService:
    def __init__(self):
        self.caches = {}

    def get_cache(self, cache_name: str, initiator_type: type, initiator_data: list or int = None) -> Cache:
        if cache_name not in self.caches:
            self.caches[cache_name] = Cache(initiator_type, initiator_data)
        return self.caches[cache_name]

    def clear_cache(self, cache_name: str):
        if cache_name in self.caches:
            self.caches[cache_name].clear()

    def clear_all_caches(self):
        for cache in self.caches.values():
            cache.clear()

    def clear_expired_caches(self, expiration_time: int):
        for cache in self.caches.values():
            cache.clear_expired(expiration_time)

    def inspect(self):
        caches = dict()

        for name, cache in self.caches.items():
            caches[name] = cache.inspect()

        return {
            "caches": caches,
            "size": self.size,
        }

    @property
    def size(self):
        total_size = 0

        for cache in self.caches.values():
            total_size += cache.size

        return total_size
