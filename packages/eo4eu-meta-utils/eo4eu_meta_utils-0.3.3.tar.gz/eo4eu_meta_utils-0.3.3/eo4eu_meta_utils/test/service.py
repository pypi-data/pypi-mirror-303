from pathlib import Path
from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic

from .logs import logger
from .message import KafkaMessage


def _ack(err, msg):
    if err is not None:
        logger.error(
            f"Failed to deliver message: {str(msg.value())}: {str(err)}"
        )
    else:
        logger.info(
            f"Message produced: {str(msg.value())} on topic {msg.topic()}"
        )

class Service:
    def __init__(
        self,
        admin_config: dict,
        producer_config: dict,
        consumer_config: dict,
        inputs: list[KafkaMessage],
        outputs: list[KafkaMessage],
    ):
        self._admin_config = admin_config
        self._producer_config = producer_config
        self._consumer_config = consumer_config
        self._inputs = inputs
        self._outputs = outputs

    def create_topics(self):
        admin = AdminClient(self._admin_config)
        all_topics = [
            NewTopic(item.topic())
            for item in self._inputs + self._outputs
        ] 
        topic_futures = admin.create_topics(all_topics)

        created_topics = []
        for topic, future in topic_futures.items():
            future.result()
            created_topics.append(topic)
            logger.info(f"Topic created: {topic}")

        for topic in all_topics:
            if topic.topic not in created_topics:
                logger.error(f"Failed to create topic: {topic.topic}")

    def produce(self):
        producer = Producer(self._producer_config)
        for message in self._inputs:
            producer.produce(
                message.topic(),
                value = message.json(),
                callback = _ack
            )
            producer.flush()

    def consume(self):
        consumer = Consumer(self._consumer_config)
        try:
            consumer.subscribe([
                output.topic() for output in self._outputs
            ])

            while True:
                msg = consumer.poll(timeout = 1.0)
                if msg is None or msg.error():
                    continue
                self.handle(msg.topic(), msg.value().decode("utf-8"))
        finally:
            consumer.close()

    def handle(self, topic: str, msg: str):
        logger.info(f"new message received: {msg} from topic {topic}")
