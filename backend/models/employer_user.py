from .user import User


class EmployerUser(User):
    dto_fields = ['_id', 'type', 'name', 'pic', 'about', 'location', 'is_employee', 'is_employer']
    is_employee = False
    is_employer = True

    def __init__(self, data):
        super(User, self).__init__(data)
