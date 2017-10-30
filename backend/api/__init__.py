import traceback

from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.errorhandler(Exception)
def error(error):
    return jsonify({'success': False, 'message': traceback.format_exc()})

class Endpoints:
    import api.auth
    import api.user
    import api.position
    import api.request