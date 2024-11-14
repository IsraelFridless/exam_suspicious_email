from pymongo import MongoClient

from app.settings.mongo_config import DB_URL

client = MongoClient(DB_URL)

db = client['suspicious_emails']

messages_collection = db['messages']