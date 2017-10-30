from flask import request,jsonify
from flask_login import current_user
from flask_pymongo import ObjectId
from api import api
from repositories import RequestRepository

update_fields = ['name', 'about', 'skills']


@api.route("/requests", methods=["POST"])
def create_request():
    employee_id = current_user._id if current_user.type == "employee" else ObjectId(request.json['recipient'])
    employer_id = current_user._id if current_user.type == "employer" else ObjectId(request.json['recipient'])
    req = RequestRepository.insert({
        'employer_id': employer_id,
        'employee_id': employee_id,
        'position_id': ObjectId(request.json['position'])
    })
    return jsonify({'success': True, 'request': req.get_dto()})
