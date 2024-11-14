from app.repository.postgres_repository.device_repository import insert_device
from app.repository.postgres_repository.location_repository import insert_location
from app.repository.postgres_repository.message_repository import insert_message
from app.repository.postgres_repository.sentence_hostage_repository import insert_many_hostage_sentences
from app.utils.data_handling import *


def process_hostage_message(message: dict):
    location: Location = message_to_location(message)
    device: Device = message_to_device(message)

    location_id: int = insert_location(location)
    device_id: str = insert_device(device)
    message_details: Message = convert_data_to_message(message, location_id, device_id)

    insert_message(message_details)

    sentences: List[SentenceHostage] = message_to_hostage_sentences(message)

    insert_many_hostage_sentences(sentences)