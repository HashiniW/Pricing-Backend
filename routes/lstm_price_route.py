from flask import Flask
from flask import Blueprint
from flask_restful import Api
from resources.lstm_price_resource import Predict

lstm_blueprint = Blueprint('lstm', __name__)
lstm_blueprint_api = Api(lstm_blueprint)

lstm_blueprint_api.add_resource(Predict, '/vegetable', methods=['GET'])
lstm_blueprint_api.add_resource(Predict, '/user', methods=['POST'])


