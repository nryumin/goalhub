from .user import UserRepository
from .position import PositionRepository
from .request import RequestRepository

from flask_login import current_user


def get_frontend_data():
    data = {}
    data['currentUser'] = current_user.get_dto()

    requests = RequestRepository.get_by_recipient_id(current_user._id)
    data['requests'] = []
    users_to_fetch = []
    for req in requests:
        data['requests'].append(req.get_dto())
        users_to_fetch.append(req.employer_id if current_user.is_employee else req.employee_id)

    users = UserRepository.get_by_ids(users_to_fetch)
    data['users'] = list(map(lambda u: u.get_dto(), users))

    if current_user.is_employer:
        data['positions'] = PositionRepository.get_by_employer_id(current_user._id)
    else:
        ids = map(lambda req: req.position_id, requests)
        data['positions'] = PositionRepository.get_by_ids(ids)
    data['positions'] = list(map(lambda p: p.get_dto(), data['positions']))
    return data

