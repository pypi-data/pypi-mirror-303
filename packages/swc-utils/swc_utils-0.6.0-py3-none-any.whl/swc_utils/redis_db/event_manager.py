import uuid
import pickle
from redis import Redis
from flask import Flask
from threading import Thread
from swc_utils.caching import CachingService


class SessionEventManager:
    def __init__(self, app: Flask, redis: Redis, redis_cache: CachingService, data_lifetime=10, host=False):
        self.app = app
        self.redis = redis
        self.cache = redis_cache.get_cache("redis-event-manager", dict)
        self.__events = {}
        self.__data_lifetime = data_lifetime

        if host:
            self._start()

    def _start(self):
        try:
            import gevent
            from gevent import monkey

            monkey.patch_all()
            gevent.spawn(self.__thread, self.app)
        except ImportError:
            self.app.logger.warn("REDIS EM Gevent not found, using threading instead. This is not recommended!")
            Thread(target=self.__thread, args=(self.app,), daemon=True).start()

    # Event handling ----------------------------------------------------------

    def on_callback(self, channel: str, callback: callable, *args, **kwargs):
        if channel in self.__events:
            raise Exception(f"Event {channel} already exists")

        self.__events[channel] = lambda data: callback(data, *args, **kwargs)

    def on(self, channel: str) -> callable:
        def decorator(func, *args, **kwargs):
            self.on_callback(channel, func, *args, **kwargs)

        return decorator

    def off(self, channel):
        self.__events.pop(channel)

    def __call_callback(self, channel: str, data: any) -> any:
        if channel not in self.__events:
            return

        return self.__events[channel](data)

    def __thread(self, app: Flask):
        pubsub = self.redis.pubsub()
        pubsub.subscribe("session-queries")

        for message in pubsub.listen():
            if message["type"] == "message":
                query = pickle.loads(message["data"])
                query_id = query.get("id")
                channel = query.get("channel")
                req = query.get("req")

                with app.app_context():
                    app.logger.info(f"REDIS [{channel}] {req}")
                    response = app.ensure_sync(self.__call_callback)(channel, req)

                response_key = f"session-response:{query_id}"
                self.redis.publish(response_key, pickle.dumps({"id": query_id, "res": pickle.dumps(response)}))

    # Event sending -----------------------------------------------------------

    @staticmethod
    def __parse_response(response: any) -> any:
        if type(response) is bytes:
            return pickle.loads(response)
        return response

    def query(self, channel: str, data: any) -> any:
        cache_key = f"{channel}:{data}"
        self.cache.clear_expired(self.__data_lifetime)
        if cache_hit := self.cache.get(cache_key):
            return self.__parse_response(cache_hit)

        query_id = str(uuid.uuid4())
        response_key = f"session-response:{query_id}"

        self.redis.publish("session-queries", pickle.dumps({"id": query_id, "channel": channel, "req": data}))

        pubsub = self.redis.pubsub()
        pubsub.subscribe(response_key)

        for message in pubsub.listen():
            if message["type"] == "message":
                response = pickle.loads(message["data"])
                if response.get("id") != query_id:
                    continue

                resp_data = response.get("res")
                if resp_data is not None:
                    self.cache[cache_key] = resp_data
                    return self.__parse_response(resp_data)

        return None

