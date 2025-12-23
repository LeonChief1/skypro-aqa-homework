from sqlalchemy import create_engine
from sqlalchemy.sql import text

class HomeWorkDb:
    __scripts = {
        "select": "select * from employee where deleted_at is null",
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into employee (\"first_name\", \"last_name\", \"middle_name\", \"company_id\", \"email\", \"phone\", \"birthdate\", \"is_active\") values (:first_name, :last_name, :middle_name, :company_id, :email, :phone, :birthdate, :is_active)"),
        "get max id": "select MAX(\"id\") from employee where is_active is True",
        "select by id": text("select * from employee where id =:select_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_employees(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def delete(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    def create(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active):
        self.__db.execute(self.__scripts["insert new"], first_name = first_name, last_name = last_name, middle_name = middle_name, company_id = company_id, email = email, phone = phone, birthdate = birthdate, is_active = is_active)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]
    
    def get_employee_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id = id).fetchall()[0]
    
    def get_employee_by_id_list(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id = id).fetchall()