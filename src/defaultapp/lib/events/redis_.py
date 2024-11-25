import redis


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

	def set(self, key, value):
		return self._client.set(key, value)

	def get(self, key):
		return self._client.get(key)
