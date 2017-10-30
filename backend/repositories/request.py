from flask_login import current_user
import app
import datetime
from models import Request
from functools import reduce


class RequestRepository:
    @classmethod
    def insert(cls, data):
        data['employee_read'] = current_user.type == 'employee'
        data['employer_read'] = current_user.type == 'employer'
        data['created'] = datetime.datetime.now()
        id = app.mongo.db.requests.insert(data)
        return Request(app.mongo.db.requests.find_one({'_id': id}))

    @classmethod
    def get_by_recipient_id(cls, id):
        query = {
            '$or': [
                {'employee_id': id},
                {'employer_id': id}
            ]
        }
        requests = app.mongo.db.requests.find(query)
        requests = list(map(lambda p: Request(p), requests))
        return requests
