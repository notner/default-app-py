def test_basic_ctx(test_ctx):
	assert test_ctx.environ == 'test'


def test_redis_access(test_ctx):
	assert test_ctx.redis.set('foo', 'boo')
	assert test_ctx.redis.get('foo') == b'boo'


def test_kafka_access(test_ctx):
	assert test_ctx.kafka.send('boo') is None
