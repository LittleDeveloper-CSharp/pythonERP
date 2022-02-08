from datetime import date

import jinja2
import os.path

from DTO.doc import Doc
from DTO.rent_doc import RentDoc, ResidentForDoc, ObjectForDoc
from Models.connect_data_base import cur, conn
from docxtpl import DocxTemplate

from Models.resident_object import create_doc_for_user


def get_residents():
    return cur.execute("SELECT * FROM resident").fetchall()


def get_object():
    return cur.execute("SELECT * FROM object").fetchall()


def __convert_date_for_sqlite(date_with_dot):
    date_mas = date_with_dot.split('.')
    return date(int(date_mas[2]), int(date_mas[1]), int(date_mas[0])).isoformat()


def get_entity_for_report(date_start, date_end, entity):
    converted_date_start = __convert_date_for_sqlite(date_start)
    converted_date_end = __convert_date_for_sqlite(date_end)

    return cur.execute("SELECT r.id, rt.lastName || ' ' || rt.firstName || ' ' || rt.patronymic as fullname, o.name, "
                       "dateStart, dateEnd, totalSum, s.title, purposeOfTheLease "
                       "FROM rent as r INNER JOIN status as s ON s.id = r.idStatus "
                       "INNER JOIN resident as rt on rt.id = r.idResident "
                       "INNER JOIN object as o on o.id = r.idObject "
                       f"WHERE {entity[1]} = '{entity[0]}' "
                       f"and date(substr(dateStart, 7) || '-' || substr(dateStart, 4, 2) || '-' || "
                       f"substr(dateStart, 1, 2)) >= date('{converted_date_start}') "
                       f"and date(substr(dateStart, 7) || '-' || "
                       f"substr(dateStart, 4, 2) || '-' || substr(dateStart, 1, 2)) <= date('{converted_date_end}')",
                       ).fetchall()


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

        path_module = os.path.abspath(__file__).split('\\')
        root_path = '\\'.join(path_module[0:len(path_module) - 2])

        resident_id = cur.execute("SELECT idResident FROM rent WHERE id = ?", (rent_id,)).fetchone()

        login_resident = cur.execute("SELECT login FROM resident WHERE id = ?", resident_id).fetchone()[0]

        resident = __get_resident_info_for_doc(rent_id)

        rent_object = __get_object_info_for_doc(rent_id)

        date_rent = __get_day_info_for_doc(rent_id)

        rentDoc = RentDoc()

        rentDoc.set_resident(resident)
        rentDoc.set_object(rent_object)
        rentDoc.set_day(date_rent['start'], date_rent['end'])

        doc_rent = Doc((0, f"Договор аренды {object_id}", "Договор аренды", login_resident,
                        f"/Resources/docs/{login_resident}/Договор аренды {object_id}.docx"))

        doc = DocxTemplate(f"{root_path}/Resources/template/temp_doc.docx")
        doc_context = dict(**dict(rentDoc.__dict__))
        doc.render(doc_context)
        doc.save(f"{root_path}{doc_rent.path}")

        doc_rent.path = f"..{doc_rent}"

        create_doc_for_user(doc_rent)

    conn.commit()


def __get_resident_info_for_doc(rent_id):
    resident_id = cur.execute("SELECT idResident FROM rent WHERE id = ?", (rent_id,)).fetchone()

    resident = cur.execute("SELECT lastName, firstName, patronymic, bik, bank, inn, kpp, address, payAcc, 'index',"
                           " email, corAcc, birthday, ipName, passport, passport_issued, passport_date_issued,"
                           " certificate_number FROM resident INNER JOIN resident_details_info"
                           " ON resident.id = resident_details_info.resident_id "
                           " WHERE resident.id = ?", resident_id).fetchone()
    return ResidentForDoc(resident)


def __get_object_info_for_doc(rent_id):
    object_id, total_sum, purpose_of_the_lease = cur.execute(
        "SELECT idObject, totalSum, purposeOfTheLease FROM rent WHERE id = ?", (rent_id,)).fetchone()

    cadastral_number, object_square = cur.execute("SELECT cadastralNumber, area FROM object WHERE id = ?",
                                                  (object_id,)).fetchone()

    return ObjectForDoc((cadastral_number, object_square, purpose_of_the_lease, total_sum))


def __get_day_info_for_doc(rent_id):
    dates = cur.execute("SELECT dateStart, dateEnd FROM rent WHERE id = ?", (rent_id,)).fetchone()
    return {'start': dates[0], 'end': dates[1]}


def accept_update_resident(resident, status):
    if status == 1:
        is_update = cur.execute("SELECT id FROM resident WHERE login = ?", (resident.login,)).fetchone() \
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
    cur.execute("DELETE FROM object WHERE id = ?", (object_id,))
    conn.commit()


def update_object(object_info):
    cur.execute("UPDATE object SET name = ?, price = ?, area = ?, photoPath = ? WHERE id = ?",
                (object_info.Name, object_info.rentPrice, object_info.Area, object_info.photo_path, object_info.Id))
    conn.commit()


def create_object(object_info):
    cur.execute("INSERT INTO object (name, price, area, photoPath, idStatus) VALUES (?, ?, ?, ?, ?)",
                (object_info.Name, object_info.rentPrice, object_info.Area, object_info.photo_path, 4))
    conn.commit()
