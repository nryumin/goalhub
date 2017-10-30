from flask_pymongo import ObjectId
from pymongo import ReturnDocument
import app
from models import EmployeeUser, EmployerUser


def get_user_from_data(data):
    if not data:
        print("None")
        return None
    if data['type'] == 'employee':
        return EmployeeUser(data)
    elif data['type'] == 'employer':
        return EmployerUser(data)
    raise Exception("Bad user type: {}".format(data['type']))


class UserRepository:
    @classmethod
    def get_by_id(cls, user_id):
        user = app.mongo.db.users.find_one({'_id': ObjectId(user_id)})
        return get_user_from_data(user)

    @classmethod
    def get_by_email(cls, email):
        user = app.mongo.db.users.find_one({'email': email})
        return get_user_from_data(user)

    @classmethod
    def get_by_token(cls, token):
        user = app.mongo.db.users.find_one({'confirm_token': token})
        return get_user_from_data(user)

    @classmethod
    def get_by_ids(cls, user_ids):
        user_ids = map(ObjectId, user_ids)
        users = app.mongo.db.users.find({'_id': {'$in': list(user_ids)}})
        return list(map(get_user_from_data, users))

    @classmethod
    def insert(cls, user_data):
        if user_data['type'] == 'employee' and "currency" not in user_data:
            user_data['currency'] = "eur"
        id = app.mongo.db.users.insert(user_data)
        return cls.get_by_id(id)

    @classmethod
    def update(cls, query, data):
        user = app.mongo.db.users.find_one_and_update(query, data, return_document=ReturnDocument.AFTER)
        return get_user_from_data(user)

    @classmethod
    def search_employees(cls, query):
        users = app.mongo.db.users.find({'type': 'employee', 'confirmed': True})
        return list(map(get_user_from_data, users))

    # @classmethod
    # def all(cls, query):
    #     users = app.mongo.db.users.find({'type': 'employee', 'confirmed': True})
    #     return list(map(get_user_from_data, users))

