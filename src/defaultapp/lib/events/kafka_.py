import json

from kafka import KafkaConsumer
from kafka import KafkaProducer


class KafkaClient:
	def __init__(
		self,
		servers: list[str],
		topic: str
	):
		self.__servers = servers if servers else ['localhost:9092']
		self.__topic = topic
		self.__producer = KafkaProducer(
			bootstrap_servers=servers
		)
		self.__consumer = KafkaConsumer(
			bootstrap_servers=servers
		)

	def send(self, message: str):
		self.__producer.send(
			self.__topic,
			json.dumps({'message': message}).encode("utf-8"),
		)

	def consume(self):
		self.__consumer.subscribe(self.__topic)
		while 1:
			try:
				r = self.__consumer.poll(timeout_ms=1000)
				for topic_data, con_rs in r.items():
					for con_r in con_rs:
						print(f'{topic_data} {con_r=}')
				continue
			except Exception as e:
				print(e)
				continue
