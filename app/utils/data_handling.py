from typing import List

from app.db.postgres_db.models import Message, SentenceExplosive, Device, Location, SentenceHostage


def message_to_device(message: dict, message_id) -> Device:
    device_info = message['device_info']
    return Device(
        browser=device_info['browser'],
        os=device_info['os'],
        message_id=message_id
    )

def message_to_explosive_sentences(message: dict, message_id) -> List[SentenceExplosive]:
    sentences = message['sentences']
    return [SentenceExplosive(
        sentence=sentence,
        message_id=message_id
    ) for sentence in sentences]

def convert_data_to_message(message: dict) -> Message:
    return Message(
        username=message['username'],
        email=message['email'],
        ip_address=message['ip_address'],
        message_created_at=message['created_at'],
    )

def message_to_location(message: dict, message_id) -> Location:
    location_info = message['location']
    return Location(
        city=location_info['city'],
        country=location_info['country'],
        longitude=location_info['longitude'],
        latitude=location_info['latitude'],
        message_id=message_id
    )

def message_to_hostage_sentences(message: dict, message_id) -> List[SentenceHostage]:
    sentences = message['sentences']
    return [SentenceHostage(
        sentence=sentence,
        message_id=message_id
    ) for sentence in sentences]

def rearrange_sentences(message: dict) -> dict:
    key_words = ['hostage', 'explosive']
    message['sentences'].sort(key=lambda sentence: 0 if any(word in sentence for word in key_words) else 1)
    return message

def message_to_dict(message: Message):
    return {
        "id": message.id,
        "username": message.username,
        "email": message.email,
        "ip_address": message.ip_address,
        "created_at": message.message_created_at,
        "device_info": {
            "os": message.device.os,
            "browser": message.device.browser
        } if message.device else None,
        "location": {
            "city": message.location.city,
            "country": message.location.country,
            "latitude": message.location.latitude,
            "longitude": message.location.longitude
        } if message.location else None,
        "hostage_sentences": [s.sentence for s in message.hostage_sentences],
        "explosive_sentences": [s.sentence for s in message.explosive_sentences]
    }
