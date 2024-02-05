import repository
from models import Users
import utils


def create_user(_user: Users):
    print('St')
    _user.password = utils.hash_string(_user.password)
    print('En')
    return repository.create_user(_user)


def get_user(_user_name, _password):
    password = utils.hash_string(password)
    user = repository.get_user(_user_name, _password)
    if user is None:
        return None, "Incorrect username or password"
    return user.id, None
