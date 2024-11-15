import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)

def produce_message(message: dict):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode()
    )
    producer.send(
        topic=os.environ['TOPIC_ALL_MESSAGES_NAME'],
        key=message['id'].encode('utf-8'),
        value=message
    )
    print(f'Sent message: {message}')
    producer.flush()