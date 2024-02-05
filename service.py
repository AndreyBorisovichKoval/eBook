import repository
from models import Users
import utils


def create_user(_user: Users):
    Users.password = utils.hash_string(Users.password)
    return repository.create_user(_user)


def get_user(_username, _password):
    password = utils.hash_string(password)
    user = repository.get_user(_username, _password)
    if user is None:
        return None, "Incorrect username or password"
    return user.id, None
