from redis import Redis
from flask import Flask, current_app
from flask_session import Session
from swc_utils.caching import CachingService
from swc_utils.redis_db.event_manager import SessionEventManager


def get_app_redis_interface(app: Flask = current_app) -> "AppRedisInterface":
    return app.config["APP_REDIS_INTERFACE"]


class AppRedisInterface:
    def __init__(self, app: Flask, is_host: bool = False,
                 redis_host="127.0.0.1", redis_port=6379, redis_db=0, redis_unix_socket_path=None,
                 cache: CachingService = None):
        self.app = app

        self.__redis_session = Redis(host=redis_host, port=redis_port, db=redis_db) \
            if redis_unix_socket_path is None else Redis(unix_socket_path=redis_unix_socket_path)
        self.__redis_cache = cache or CachingService()

        self.__event_manager = SessionEventManager(self.app, self.__redis_session, self.__redis_cache, host=is_host)

        self.__initialize_on_app()

    def __initialize_on_app(self):
        self.app.config["SESSION_TYPE"] = "redis"
        self.app.config["SESSION_SERIALIZATION_FORMAT"] = "json"
        self.app.config["SESSION_REDIS"] = self.__redis_session
        self.app.config["APP_REDIS_INTERFACE"] = self
        Session(self.app)

    @property
    def redis_session(self) -> Redis:
        return self.__redis_session

    @property
    def event_manager(self) -> SessionEventManager:
        return self.__event_manager

    @property
    def redis_cache(self) -> CachingService:
        return self.__redis_cache
