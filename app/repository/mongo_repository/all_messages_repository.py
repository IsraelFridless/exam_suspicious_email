from app.db.mongo_db.database import messages_collection


def insert_message(message_data: dict):
    messages_collection.insert_one(message_data)