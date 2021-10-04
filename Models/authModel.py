from Models.ConnectDataBase import cur

def AuthorizationUser(login, password):
    return cur.execute(f"SELECT idResident FROM user WHERE login = '{login}' AND password = '{password}'").fetchone()
