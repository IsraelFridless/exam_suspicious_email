import json
import os
import sys

from dotenv import load_dotenv
from kafka import KafkaConsumer


load_dotenv(verbose=True)

def consume_explosive_message():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EXPLOSIVE_MESSAGES_NAME'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )
    for message in consumer:
        print(message)


if __name__ == '__main__':
    try:
        consume_explosive_message()
    except KeyboardInterrupt:
        print('interrupted')
        sys.exit(0)