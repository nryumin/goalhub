from flask_pymongo import ObjectId
import datetime
import app
import re
from models import Position


class PositionRepository:
    @classmethod
    def get_by_employer_id(cls, id):
        positions = app.mongo.db.positions.find({'employer_id': ObjectId(id)})
        positions = list(map(lambda p: Position(p), positions))
        return positions

    @classmethod
    def get_by_id(cls, id):
        position = app.mongo.db.positions.find_one({'_id': ObjectId(id)})
        position = Position(position)
        return position

    @classmethod
    def get_by_ids(cls, ids):
        ids = list(map(ObjectId, ids))
        positions = app.mongo.db.positions.find({'_id': {'$in': ids}})
        return list(map(Position, positions))

    @classmethod
    def search(cls, query=None):
        if query:
            regx = re.compile(query, re.IGNORECASE)
            query = {
                '$or': [
                    {'name': regx},
                    {'about': regx}
                ]
            }
        else:
            query = {}
        positions = app.mongo.db.positions.find(query)
        positions = list(map(lambda p: Position(p), positions))
        return positions

    @classmethod
    def insert(cls, data):
        data['created'] = datetime.datetime.now()
        id = app.mongo.db.positions.insert(data)
        return Position(app.mongo.db.positions.find_one({'_id': id}))
