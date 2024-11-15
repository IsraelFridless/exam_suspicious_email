from flask import Blueprint, request, jsonify

from app.service.messages_service import is_hostage_message, is_explosive_message
from app.service.producers_service.all_messages import produce_message
from app.service.producers_service.explosive_messages import produce_explosive_message
from app.service.producers_service.hostage_messages import produce_hostage_message
from app.utils.data_handling import rearrange_sentences

data_receiver_blueprint = Blueprint('data_receiver', __name__)

@data_receiver_blueprint.route('/', methods=['POST'])
def receive_data():
    try:
        message = request.json

        produce_message(message)

        sentences_ordered_message = rearrange_sentences(message)

        if is_hostage_message(message):
            produce_hostage_message(sentences_ordered_message)

        elif is_explosive_message(message):
            produce_explosive_message(sentences_ordered_message)

        return jsonify({'message': 'received request'}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500