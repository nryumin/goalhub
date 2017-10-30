from .entity_base import EntityBase


class Position(EntityBase):
    dto_fields = ['_id', 'name', 'about', 'skills', 'salary', 'created', 'location', 'employer_id', 'position_id', 'created']

    def __init__(self, data):
        super(Position, self).__init__(data)

    def get_dto(self):
        dto = super(Position, self).get_dto()
        dto['employer_id'] = str(dto['employer_id'])
        return dto
