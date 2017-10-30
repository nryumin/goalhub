from flask import request,jsonify
from flask_login import current_user
from flask_pymongo import ObjectId
from api import api
from repositories import UserRepository

update_fields = {
    'employee': ['skills', 'birthday', 'salary', 'about', 'pic', 'currency', 'work', 'education'],
    'employer': ['name', 'pic', 'about'],
}


@api.route("/user", methods=["PUT"])
def update_user():
    data = {}
    for field in update_fields[current_user.type]:
        if field in request.json:
            data[field] = request.json[field]

    user = UserRepository.update({'_id': ObjectId(current_user._id)}, {'$set': data})
    return jsonify({'success': True, 'user': user.get_dto()})


@api.route("/search-employees", methods=["GET"])
def search_candidates():
    query = request.args.get('query')
    employees = UserRepository.search_employees(query)
    employees = list(map(lambda e: e.get_dto(), employees))
    return jsonify({'success': True, 'employees': employees})

# @api.route("/search-employees/all", methods=["GET"])
# def search_candidates():
#     query = request.args.get('query')
#     employees = UserRepository.all(query)
#     employees = list(map(lambda e: e.get_dto(), employees))
#     return jsonify({'success': True, 'employees': employees})
