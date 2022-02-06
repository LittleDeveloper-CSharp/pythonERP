from Models.connect_data_base import cur, conn


def get_residents():
    return cur.execute("SELECT * FROM resident").fetchall()


def get_wait_rent_list():
    return cur.execute("SELECT r.id, res.lastName || ' ' || res.firstName FROM rent as r "
                       "INNER JOIN resident as res ON res.id = r.idResident "
                       "WHERE r.idStatus = '2'").fetchall()


def get_resident_for_update(request_id):
    resident_for_update = cur.execute("SELECT * FROM resident_wait_update WHERE id = ?", (request_id,)).fetchone()
    resident = cur.execute("SELECT * FROM resident WHERE login = ?", (resident_for_update[1],)).fetchone()
    return resident, resident_for_update


def get_wait_update_list():
    return cur.execute("SELECT resident_wait_update.id, resident.lastName || ' ' || resident.firstName "
                       "FROM resident_wait_update "
                       "LEFT JOIN resident ON resident.login = resident_wait_update.login")


def create_resident(resident):
    cur.execute("INSERT INTO resident (login, lastName, firstName, patronymic, inn, phone, email, photoPath)"
                f" VALUES ('{resident.login}', '{resident.last_name}', '{resident.first_name}', '{resident.patronymic}'"
                f", '{resident.inn}', '{resident.phone}', '{resident.email}', '{resident.photo_path}')")
    conn.commit()


def get_request_by_rent(rent_id):
    return cur.execute("SELECT r.id, r.idResident, r.idObject, r.dateStart, r.dateEnd, r.totalSum, r.idStatus, "
                       "o.area, o.photoPath FROM rent as r "
                       "INNER JOIN object as o ON o.id = r.idObject WHERE r.id = ?", (rent_id,)).fetchone()


def get_resident(resident_id):
    return cur.execute("SELECT * FROM resident WHERE id = ?", (resident_id,)).fetchone()


def update_property_rent(rent_id, status):
    object_id = cur.execute(f"SELECT idObject FROM rent  WHERE id = {rent_id}").fetchone()[0]
    cur.execute(f"UPDATE rent SET idStatus = {status} WHERE id = '{rent_id}'")

    if status == 3:
        cur.execute(f"UPDATE object SET idStatus = '4' WHERE id = '{object_id}'")
    else:
        cur.execute(f"UPDATE object SET idStatus = '1' WHERE id = '{object_id}'")
    conn.commit()


def accept_update_resident(resident, status):
    if status == 1:
        is_update = cur.execute("SELECT id FROM resident WHERE login = ?", (resident.login, )).fetchone() \
                    is not None
        if is_update:
            cur.execute("UPDATE resident SET lastName = ?, firstName = ?, patronymic = ?, inn = ?, "
                        "phone = ?, photoPath = ?, email = ? WHERE login = ?",
                        (resident.last_name, resident.first_name, resident.patronymic, resident.inn,
                         resident.phone, resident.photo_path, resident.email, resident.login))
        else:
            cur.execute(f"INSERT INTO resident SELECT * FROM resident_wait_update WHERE id = '{resident.Id}'")

        cur.execute(f"UPDATE user SET isActive = 1 WHERE login = '{resident.login}'")
    cur.execute(f"DELETE FROM resident_wait_update WHERE id = '{resident.Id}'")
    conn.commit()


def delete_object(object_id):
    cur.execute("DELETE FROM object WHERE id = '?'", (object_id, ))
    conn.commit()


def update_object(object_info):
    cur.execute("UPDATE object SET name = ?, price = ?, area = ?, photoPath = ? WHERE id = ?",
                (object_info.Name, object_info.rentPrice, object_info.Area, object_info.photo_path, object_info.Id))
    conn.commit()


def create_object(object_info):
    cur.execute("INSERT INTO object (name, price, area, photoPath, idStatus) VALUES (?, ?, ?, ?, ?)",
                (object_info.Name, object_info.rentPrice, object_info.Area, object_info.photo_path, 4))
    conn.commit()
