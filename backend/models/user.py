from flask_login import UserMixin
from .entity_base import EntityBase


class User(UserMixin, EntityBase):
    def __init__(self, data):
        super(EntityBase, self).__init__(data)

    def get_id(self):
        return str(self._id)
