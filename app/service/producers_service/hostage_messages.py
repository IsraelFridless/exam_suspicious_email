import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)

def produce_hostage_message(message: dict):

    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode()
    )
    producer.send(
        topic=os.environ['TOPIC_HOSTAGE_MESSAGES_NAME'],
        key=message['id'].encode('utf-8'),
        value=message
    )
    print(f'Contained hostage message sent: {message}')
    producer.flush()