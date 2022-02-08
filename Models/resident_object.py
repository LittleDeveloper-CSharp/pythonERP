import datetime

from Models.connect_data_base import cur, conn


def get_rent_object(resident_id):
    return cur.execute("SELECT o.id, o.name, o.area, r.dateStart, r.dateEnd, r.totalSum, o.photoPath, r.idStatus"
                       " FROM rent as r"
                       " LEFT JOIN object as o ON o.id = r.idObject"
                       f" WHERE idResident = {resident_id} and o.idStatus != 3 and r.idStatus != 3").fetchall()


def resident_objects(resident_id, object_id, date_start_srt, date_end_srt, reason):
    cur.execute(f"UPDATE object SET idStatus = '2' WHERE id = '{object_id}'")

    rent_day = cur.execute(f"SELECT price FROM object WHERE id = '{object_id}'").fetchone()[0]

    date_tuple = date_start_srt.split('.')
    date_start = datetime.date(year=int(date_tuple[2]), month=int(date_tuple[1]), day=int(date_tuple[0]))

    date_tuple = date_end_srt.split('.')
    date_end = datetime.date(year=int(date_tuple[2]), month=int(date_tuple[1]), day=int(date_tuple[0]))

    count_days = date_end - date_start
    rent_sum = count_days.days * rent_day

    cur.execute(f"INSERT INTO rent (idResident, idObject, dateStart, dateEnd, idStatus, totalSum, purposeOfTheLease) "
                f"VALUES ('{resident_id}', '{object_id}', '{date_start_srt}', '{date_end_srt}', '2', '{rent_sum}', "
                f"'{reason}')")
    conn.commit()


def cancellation_rent(resident_id, object_id):
    cur.execute(f"UPDATE object SET idStatus = '4' WHERE id = '{object_id}'")
    cur.execute(f"UPDATE rent SET idStatus = '3' WHERE idResident = '{resident_id}' and idObject = '{object_id}'"
                f" and idStatus = '2'")
    conn.commit()


def create_profile(resident, password):
    cur.execute("INSERT OR IGNORE INTO user (login, password, isActive, idRole) VALUES (?, ?, 0, 2)", (resident.login,
                                                                                                       password))
    conn.commit()


def edit_profile(resident_info, password):
    if resident_info.Id == 0:
        create_profile(resident_info, password)

    flag = cur.execute('SELECT id FROM resident_wait_update WHERE login = ?', (resident_info.login,)).fetchone()
    if flag is None:
        cur.execute("INSERT INTO resident_wait_update (login, lastName, "
                    "firstName, patronymic, inn, phone, email, photoPath) "
                    f"VALUES ('{resident_info.login}', '{resident_info.last_name}', '{resident_info.first_name}', "
                    f"'{resident_info.patronymic}',"
                    f"'{resident_info.inn}', '{resident_info.phone}', '{resident_info.email}', "
                    f"'{resident_info.photo_path}')")

    if password != '' and not password.isspace():
        cur.execute(f"UPDATE user SET password = '{password}' WHERE login = '{resident_info.login}'")

    conn.commit()


def get_details_info(resident_id):
    return cur.execute("SELECT * FROM resident_details_info WHERE resident_id = ?", (resident_id, )).fetchone()


def create_details_info(resident_details_info):
    cur.execute("INSERT INTO resident_details_info"
                " (resident_id, bik, bank, kpp, address, payAcc, 'index', corAcc, ipName, birthday"
                ",passport, passport_issued, passport_date_issued, certificate_number)"
                " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", resident_details_info)
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
    delete_doc(doc.Id)
    create_doc_for_user(doc)


def doc_by_id(doc_id):
    return cur.execute(f"SELECT * FROM document WHERE id = '{doc_id}'").fetchone()
