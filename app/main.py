from flask import Flask

from app.db.postgres_db.database import init_db
from app.routes.data_receiver_route import data_receiver_blueprint
from app.routes.data_retriever_route import data_retriever_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    # init_db()
    app.register_blueprint(data_receiver_blueprint, url_prefix='/api/email')
    app.register_blueprint(data_retriever_blueprint, url_prefix='/api/data')
    app.run(port=5000)