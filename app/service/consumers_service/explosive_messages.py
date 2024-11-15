import json
import os
import sys

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.service.explosive_messages_service import process_explosive_message

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
        process_explosive_message(message.value)


if __name__ == '__main__':
    try:
        consume_explosive_message()
    except KeyboardInterrupt:
        print('interrupted')
        sys.exit(0)