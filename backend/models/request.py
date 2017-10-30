from .entity_base import EntityBase


class Request(EntityBase):
    dto_fields = ['_id', 'author_id', 'created', 'employee_id', 'employer_id',
                  'employee_read', 'employer_read', 'position_id']

    def __init__(self, data):
        super(Request, self).__init__(data)

    def get_dto(self):
        dto = super(Request, self).get_dto()
        dto['employee_id'] = str(dto['employee_id'])
        dto['employer_id'] = str(dto['employer_id'])
        dto['position_id'] = str(dto['position_id'])
        return dto
