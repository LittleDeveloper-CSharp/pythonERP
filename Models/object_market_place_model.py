from Models.connect_data_base import cur


def get_objects():
    return cur.execute(f"SELECT * FROM object").fetchall()


def get_free_object():
    return cur.execute(f"SELECT * FROM object WHERE idStatus = '4'").fetchall()


def get_details_info(resident_id):
    return cur.execute(f"SELECT * FROM resident WHERE id = '{resident_id}'").fetchone()

