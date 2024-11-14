from app.repository.postgres_repository.device_repository import insert_device
from app.repository.postgres_repository.location_repository import insert_location
from app.repository.postgres_repository.message_repository import insert_message
from app.repository.postgres_repository.sentence_explosive_repository import insert_many_explosive_sentences
from app.utils.data_handling import *


def process_explosive_message(message: dict):
    message_details: Message = convert_data_to_message(message)
    message_id = insert_message(message_details)

    location: Location = message_to_location(message, message_id)
    device: Device = message_to_device(message, message_id)

    insert_location(location)
    insert_device(device)

    sentences: List[SentenceExplosive] = message_to_explosive_sentences(message, message_id)

    insert_many_explosive_sentences(sentences)

