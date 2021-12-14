from Models.ConnectDataBase import cur, conn

def GetRentObject(id):
    return cur.execute(f"SELECT * FROM rentObject WHERE residentID = {id}").fetchall()

def RentObject(resident_id, object_id):
    cur.execute(f"UPDATE freeObject SET idResident = '{resident_id}', isActive = '0' WHERE id = '{object_id}'")
    conn.commit()
