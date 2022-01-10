from flask import jsonify, Blueprint

API = Blueprint('API', __name__)


@API.route('/', methods=['GET'])
def wecolme():
    return jsonify({'data': 'success'})
