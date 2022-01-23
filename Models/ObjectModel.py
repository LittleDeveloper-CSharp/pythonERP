from Models.ConnectDataBase import cur


def get_free_object():
    return cur.execute(f"SELECT * FROM object WHERE isActive = '1'").fetchall()


def get_details_info(resident_id):
    return cur.execute(f"SELECT * FROM resident WHERE id = '{resident_id}'").fetchone()

