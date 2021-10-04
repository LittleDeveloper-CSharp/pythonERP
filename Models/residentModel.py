from Models.ConnectDataBase import cur, conn

def GetRentObject(Id):
    return cur.execute(f"SELECT * FROM rentObject WHERE residentID = '{Id}'").fetchall()

def GetFreeObject():
    return cur.execute(f"SELECT * FROM freeObject WHERE isActive = '1'").fetchall()

def GetDetailsInfo(Id):
    return cur.execute(f"SELECT * FROM resident WHERE id = '{Id}'").fetchone()

def RentObject(residentId, objectId):
    cur.execute(f"UPDATE freeObject SET idResident = '{residentId}', isActive = '0' WHERE id = '{objectId}'")
    conn.commit()
