from flask import request,jsonify
from flask_login import current_user
from flask_pymongo import ObjectId
from api import api
from repositories import PositionRepository, UserRepository

update_fields = ['name', 'about', 'skills']


@api.route("/positions", methods=["POST"])
def create_position():
    data = dict(request.json)
    data['employer_id'] = ObjectId(current_user._id)
    position = PositionRepository.insert(data)
    return jsonify({'success': True, 'position': position.get_dto()})


@api.route("/positions", methods=["GET"])
def get_positions():
    query = request.args.get('query')
    positions = PositionRepository.search(query)
    positions = list(map(lambda p: p.get_dto(), positions))
    return jsonify({'success': True, 'positions': positions})


@api.route("/positions/<id>", methods=["GET"])
def get_position(id):
    position = PositionRepository.get_by_id(id)
    if not position:
        return jsonify({'success': False, 'message': "Not found"})

    res = {'success': True, 'position': position.get_dto()}
    if current_user.is_employee:
        res['employer'] = UserRepository.get_by_id(position.employer_id)

    return jsonify(res)
