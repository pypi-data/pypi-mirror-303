import redis.asyncio as redis

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError

from .exception.internal_exception import RedisInitializeFailureException, RedisConnectFailureException


class CacheRedis:
    def __init__(self, redis_url: str):
        self.client = None
        self.redis_url = redis_url

    async def connect(self):
        try:
            connection_pool = redis.ConnectionPool.from_url(self.redis_url)
            self.client = redis.Redis(connection_pool=connection_pool)
        except Exception as e:
            raise RedisInitializeFailureException()

    async def close(self):
        if self.client:
            self.client.close()
