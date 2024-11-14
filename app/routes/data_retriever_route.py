from typing import List

from flask import Blueprint, jsonify

from app.db.postgres_db.models import Message
from app.repository.postgres_repository.message_repository import get_suspicious_data_by_email
from app.utils.data_handling import message_to_dict

data_retriever_blueprint = Blueprint('data_retriever', __name__)

@data_retriever_blueprint.route('/<email>', methods=['GET'])
def retrieve_data_by_email(email: str):
    try:
        if not email:
            return jsonify({"error": 'email must be provided'}), 400
        data: List[Message] = get_suspicious_data_by_email(email)
        result = [message_to_dict(message) for message in data]
        return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500