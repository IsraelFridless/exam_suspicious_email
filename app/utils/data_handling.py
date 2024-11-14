from typing import List

from app.db.postgres_db.models import Message, SentenceExplosive, Device, Location, SentenceHostage


def message_to_device(message: dict) -> Device:
    device_info = message['device_info']
    return Device(
        id=device_info['device_id'],
        browser=device_info['browser'],
        os=device_info['os'],
    )

def message_to_explosive_sentences(message: dict) -> List[SentenceExplosive]:
    sentences = message['sentences']
    return [SentenceExplosive(
        sentence=sentence,
        message_id=message['id']
    ) for sentence in sentences]

def convert_data_to_message(message: dict, location_id, device_id) -> Message:
    return Message(
        id=message['id'],
        username=message['username'],
        email=message['email'],
        ip_address=message['ip_address'],
        message_created_at=message['created_at'],
        location_id=location_id,
        device_id=device_id
    )

def message_to_location(message: dict) -> Location:
    location_info = message['location']
    return Location(
        city=location_info['city'],
        country=location_info['country'],
        longitude=location_info['longitude'],
        latitude=location_info['latitude'],
    )

def message_to_hostage_sentences(message: dict) -> List[SentenceHostage]:
    sentences = message['sentences']
    return [SentenceHostage(
        sentence=sentence,
        message_id=message['id']
    ) for sentence in sentences]

def rearrange_sentences(message: dict) -> dict:
    key_words = ['hostage', 'explosive']
    message['sentences'].sort(key=lambda sentence: 0 if any(word in sentence for word in key_words) else 1)
    return message