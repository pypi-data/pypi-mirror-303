from .caching_service import CachingService


class CacheController:
    def __init__(self, cache_services: dict[str, CachingService] = None):
        self._cache_services = cache_services or dict()

    def create_cache_service(self, name: str):
        if name in self._cache_services:
            return self._cache_services[name]

        service = CachingService()
        self._cache_services[name] = service
        return service

    def clear_all(self):
        for service in self._cache_services.values():
            service.clear_all_caches()

    def clear_service(self, name: str):
        service = self._cache_services.get(name)
        if service is None:
            raise KeyError(f'Service {name} does not exist')

        service.clear_all_caches()
        
    def clear_service_cache(self, name: str, cache_name: str):
        service = self._cache_services.get(name)
        if service is None:
            raise KeyError(f'Service {name} does not exist')

        service.clear_cache(cache_name)

    def tree(self):
        service_tree = dict()

        for name, service in self._cache_services.items():
            service_tree[name] = service.inspect()

        return service_tree

    @property
    def cache_services(self):
        return self._cache_services

    @property
    def size(self):
        total_size = 0

        for service in self._cache_services.values():
            total_size += service.size

        return total_size
