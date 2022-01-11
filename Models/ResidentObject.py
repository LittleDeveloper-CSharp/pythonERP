import datetime

from Models.ConnectDataBase import cur, conn


def get_rent_object(resident_id):
    return cur.execute("SELECT o.id, o.name, o.area, r.dateStart, r.dateEnd, r.totalSum, o.photoPath, r.idStatus"
                       " FROM rent as r"
                       " LEFT JOIN object as o ON o.id = r.idObject"
                       f" WHERE idResident = {resident_id} and idStatus != 3").fetchall()


def resident_objects(resident_id, object_id, date_start_srt, date_end_srt):
    cur.execute(f"UPDATE object SET isActive = '0' WHERE id = '{object_id}'")

    rent_day = cur.execute(f"SELECT price FROM object WHERE id = '{object_id}'").fetchone()[0]

    date_tuple = date_start_srt.split('.')
    date_start = datetime.date(year=int(date_tuple[2]), month=int(date_tuple[1]), day=int(date_tuple[0]))

    date_tuple = date_end_srt.split('.')
    date_end = datetime.date(year=int(date_tuple[2]), month=int(date_tuple[1]), day=int(date_tuple[0]))

    count_days = date_end - date_start
    rent_sum = count_days.days * rent_day

    cur.execute(f"INSERT INTO rent (idResident, idObject, dateStart, dateEnd, idStatus, totalSum) "
                f"VALUES ('{resident_id}', '{object_id}', '{date_start_srt}', '{date_end_srt}', '2', '{rent_sum}')")
    conn.commit()


def cancellation_rent(resident_id, object_id):
    cur.execute(f"UPDATE object SET isActive = '1' WHERE id = '{object_id}'")
    cur.execute(f"UPDATE rent SET idStatus = '3' WHERE idResident = '{resident_id}' and idObject = '{object_id}'"
                f" and idStatus = '2'")
    conn.commit()


def edit_profile(resident_info, password):
    cur.execute(f"UPDATE resident SET lastName = '{resident_info.last_name}',"
                f"firstName = '{resident_info.first_name}', patronymic = '{resident_info.patronymic}',"
                f"inn = '{resident_info.inn}', phone = '{resident_info.phone}',"
                f"email = '{resident_info.email}', photoPath = '{resident_info.photo_path}' "
                f"WHERE id = '{resident_info.id}'")

    if password != '' and not password.isspace():
        cur.execute(f"UPDATE user SET password = '{password}' WHERE login = '{resident_info.login}'")

    conn.commit()


def docs_by_user(login):
    return cur.execute(f"SELECT * FROM document WHERE loginUser = '{login}' and isActual = '1'").fetchall()


def create_doc_for_user(doc):
    cur.execute(f"INSERT INTO document (name, description, loginUser, path) "
                f"VALUES ('{doc.name}', '{doc.description}', '{doc.user_login}', '{doc.path}')")
    conn.commit()


def delete_doc(doc_id):
    cur.execute(f"UPDATE document SET isActual = '0' WHERE id = '{doc_id}'")
    conn.commit()


def update_doc(doc):
    cur.execute(f"UPDATE document SET isActual = '0' WHERE id = '{doc.id}'")
    create_doc_for_user(doc)


def doc_by_id(doc_id):
    return cur.execute(f"SELECT * FROM document WHERE id = '{doc_id}'").fetchone()
