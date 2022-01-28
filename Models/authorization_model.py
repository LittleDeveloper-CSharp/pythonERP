from DTO.resident import Resident
from Models.connect_data_base import cur
from DTO.user import User


def authorization_user(login, password):
    user_tuple = cur.execute(f"SELECT login, idRole FROM user WHERE login = '{login}' AND password = '{password}'")\
                .fetchone()

    if user_tuple is None:
        return None

    user = User(user_tuple)

    if user.idRole == 1:
        return user

    resident = Resident(resident_details_info(user.login))

    user.set_resident(resident)

    return user


def resident_details_info(login):
    return cur.execute(f"SELECT * FROM resident WHERE login = {login}").fetchone()
