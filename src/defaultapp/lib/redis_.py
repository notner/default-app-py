import logging
import redis


log = logging.getLogger(__name__)


class RedisClient:
	def __init__(
		self,
		host: str,
		port: int,
		db: str
	):
		self._host = host
		self._port = port
		self._db = db

		pool = redis.ConnectionPool(
			host=self._host,
			port=self._port,
			db=self._db
		)
		self._client = redis.Redis(connection_pool=pool)

	def set(self, key: str, value: str, expire=None) -> bool:
		is_set = self._client.set(key, value)
		if expire:
			exp = self._client.expire(name=key, time=expire)
			if not exp:
				log.warning('failed to expire key: {key}')
		return is_set

	def get(self, key):
		return self._client.get(key)
