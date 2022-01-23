from Models.ConnectDataBase import cur


def authorization_user(login, password):
    user = cur.execute(f"SELECT login, idRole FROM user WHERE login = '{login}' AND password = '{password}'")\
        .fetchone()

    if user is None:
        return None

    if user[1] == 1:
        return user

    return user, cur.execute(f"SELECT * FROM resident WHERE login = {user[0]}")\
        .fetchone()
