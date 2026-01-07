from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure

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

    @allure.step("БД. Получение пользователей")
    def get_employees(self) -> str:
        '''
        Получение пользователей
        '''
        query = self.__db.execute(self.__scripts["select"]) #Запрос в отдельную переменную 
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("БД. Удаление пользователя по {id}")
    def delete(self, id: int) -> None:
        '''
        Удаление пользователя по id
        '''
        params = {'id_to_delete' : id}
        query = self.__db.execute(self.__scripts["delete by id"], params)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        

    @allure.step("БД. Создание пользователя {first_name}:{last_name}:{middle_name}:{company_id}:{email}:{phone}:{birthdate} -> {is_active}")
    def create(self, first_name: str, last_name: str, middle_name: str, company_id: str, email: str, phone: str, birthdate: str, is_active: bool) -> None:
        '''
        Создлание пользователя
        '''
        params = {'first_name' : first_name,
                  'last_name' : last_name,
                  'middle_name' : middle_name,
                  'company_id' : company_id,
                  'email' : email,
                  'phone' : phone,
                  'birthdate' : birthdate,
                  'is_active' : is_active
                  }
        query = self.__db.execute(self.__scripts["insert new"], params)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Получение максимального id")
    def get_max_id(self) -> str:
        '''
        Получение максимального id
        '''
        query = self.__db.execute(self.__scripts["get max id"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]
    
    @allure.step("БД. Получение пользователя по {id}")
    def get_employee_by_id(self, id: int) -> str:
        '''
        Получение пользователя по id
        '''
        params = {'select_id' : id}
        query = self.__db.execute(self.__scripts["select by id"], params)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0]
    
    @allure.step("БД. Получение пользователя по {id} из списка")
    def get_employee_by_id_list(self, id: int) -> str:
        '''
        Получение пользователя по id из списка
        '''
        params = {'select_id': id}
        query = self.__db.execute(self.__scripts["select by id"], params)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()