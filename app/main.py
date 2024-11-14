from flask import Flask

from app.routes.data_receiver_route import data_receiver_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(data_receiver_blueprint, url_prefix='/api/email')
    app.run(port=5000)