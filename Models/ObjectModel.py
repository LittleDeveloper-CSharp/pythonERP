from Models.ConnectDataBase import cur

def GetFreeObject():
    return cur.execute(f"SELECT * FROM freeObject WHERE isActive = '1'").fetchall()

def GetDetailsInfo(id):
    return cur.execute(f"SELECT * FROM resident WHERE id = '{id}'").fetchone()

