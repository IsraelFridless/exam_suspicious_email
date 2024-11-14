import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

from app.utils.data_handling import rearrange_sentences

load_dotenv(verbose=True)

def produce_explosive_message(message: dict):
    sentences_ordered_message = rearrange_sentences(message)
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode()
    )
    producer.send(
        topic=os.environ['TOPIC_EXPLOSIVE_MESSAGES_NAME'],
        key=message['id'].encode('utf-8'),
        value=sentences_ordered_message
    )
    print(f'Contained explosive message sent: {sentences_ordered_message}')
    producer.flush()