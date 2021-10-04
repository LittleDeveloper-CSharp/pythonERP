import sqlite3

conn = sqlite3.connect('./DataBase/database.db')
cur = conn.cursor()

def GetRentObject(Id):
    return cur.execute(f"SELECT * FROM rentObject WHERE residentID = {Id}").fetchall()

def GetFreeObject():
    return cur.execute("SELECT * FROM freeObject WHERE isActive = 1").fetchall()

def GetDetailsInfo(Id):
    return cur.execute(f"SELECT * FROM resident WHERE id = {Id}").fetchone()
