import pytest
from defaultapp.lib.events import KafkaClient


@pytest.fixture()
def kclient():
	k = KafkaClient(
		servers=['localhost:9092'],
		topic='very-bad'
	)
	yield k


def test_kafka_init(kclient):
	pass
