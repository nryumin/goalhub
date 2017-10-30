from .user import User

class EmployeeUser(User):
    dto_fields = ['_id', 'type', 'first_name', 'last_name', 'gender', 'pic', 'about', 'skills', 'salary', 'currency',
                  'birthday', 'education', 'location', 'work', 'external_accounts', 'is_employee', 'is_employer']
    skills = []
    external_accounts = {}
    education = []
    work = []
    is_employee = True
    is_employer = False

    def __init__(self, data):
        super(User, self).__init__(data)

    def get_dto(self):
        dto = super(User, self).get_dto()
        dto['fullname'] = dto['first_name'] + ' ' + dto['last_name']
        return dto
