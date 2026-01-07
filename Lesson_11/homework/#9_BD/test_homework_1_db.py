from HomeWorkApi import HomeWorkApi
from HomeWorkDb import HomeWorkDb
import allure

@allure.epic("Пользователи") 
@allure.severity("blocker")
class TestEmployee:

    api = HomeWorkApi("http://5.101.50.27:8000")
    db = HomeWorkDb("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

    # [GET] /employee
    @allure.story("Получение списка Пользователей")
    @allure.feature("READ")
    @allure.title("Получение полного списка пользователей")
    def test_get_employee_id(self):
        test_id=1
        result = self.db.get_employee_by_id(test_id)
        get_emloyee_id = result
        with allure.step("Проверка пользователя в компании"):
            assert get_emloyee_id["company_id"] == test_id


    # [POST] /employee
    @allure.story("Создание пользователя")
    @allure.feature("CREATE")
    @allure.title("Создание участника")
    def test_create_employee(self):
        with allure.step("Создание пользователя"):
            fist_name="Иван"
            last_name="Иванов"
            middle_name="Иванович"
            company_id = 1
            email="user@example.com"
            phone="+78005553535"
            birthdate="2025-01-01"
            is_active=True

            self.db.create(first_name=fist_name, last_name=last_name, middle_name=middle_name, company_id=company_id, email=email, phone=phone, birthdate=birthdate, is_active=is_active)

        with allure.step("Поиск последнего созданного пользователя по id"):
            max_id = self.db.get_max_id()
            if max_id is None:
                #создать запись или вернуть 0
                employees = self.db.get_employees()
                if employees:
                    max_id = self.db.get_max_id()
                else:
                    self.db.create(first_name=fist_name, last_name=last_name, middle_name=middle_name, company_id=company_id, email=email, phone=phone, birthdate=birthdate, is_active=is_active)
                    max_id = self.db.get_max_id()

        last_employee = self.api.get_employee_by_id(max_id)

        get_create_employee = last_employee

        with allure.step("Проверка полей новыго пользователя"):
            assert get_create_employee["first_name"] == "Иван"
            assert get_create_employee["last_name"] == "Иванов"
            assert get_create_employee["middle_name"] == "Иванович"
            assert get_create_employee["company_id"] == 1
            assert get_create_employee["email"] == "user@example.com"
            assert get_create_employee["phone"] == "+78005553535"
            assert get_create_employee["birthdate"] == "2025-01-01"
            assert get_create_employee["is_active"] == True
            assert len(get_create_employee) == 8

        with allure.step("Удаление созданного пользователя из БД"):
            self.db.delete(max_id)


    # [GET] /employee/{id}
    @allure.story("Получение пользователя по id")
    @allure.feature("READ")
    @allure.title("Получение участника по id")
    def test_get_employee_id_list(self):
        test_id=1
        result = self.db.get_employee_by_id_list(test_id)
        get_emloyee_id = result
        assert get_emloyee_id[-1]["company_id"] == test_id
        assert len(get_emloyee_id[-1]) == 11


    # [PATCH] /employee/{id}
    @allure.story("Изменение данных у пользователя")
    @allure.feature("UPDATE")
    @allure.title("Изменение данных с параметрами у пользователя")
    def test_change_employee(self):
        with allure.step("Создание пользователя"):
            #Создаем
            fist_name="Иван"
            last_name="Иванов"
            middle_name="Иванович"
            company_id = 1
            email="user@example.com"
            phone="+78005553535"
            birthdate="2025-01-01"
            is_active=True

            self.db.create(first_name=fist_name, last_name=last_name, middle_name=middle_name, company_id=company_id, email=email, phone=phone, birthdate=birthdate, is_active=is_active)

        with allure.step("Поиск последнего созданого пользователя по id"):
            max_id = self.db.get_max_id()
            if max_id is None:
                #создать запись или вернуть 0
                employees = self.db.get_employees()
                if employees:
                    max_id = self.db.get_max_id()
                else:
                    self.db.create(first_name=fist_name, last_name=last_name, middle_name=middle_name, company_id=company_id, email=email, phone=phone, birthdate=birthdate, is_active=is_active)
                    max_id = self.db.get_max_id()

        with allure.step("Редактирование созданного пользователя"):
            #Редактируем
            employee_id = max_id
            last_name = "Ивашка"
            email = "dfdfd@example.com"
            phone = "+79995553535"
            result = self.api.change_company_id_employee(employee_id, last_name, email, phone, True)
        get_change_employee = result
        with allure.step("Проверка корректности редактируемого пользователя."):
            assert get_change_employee["last_name"] == "Ивашка"
            assert get_change_employee["email"] == "dfdfd@example.com"
            assert get_change_employee["phone"] == "+79995553535"
            assert get_change_employee["is_active"] == True
        assert len(get_change_employee) == 8

        with allure.step("Удаление созданного пользователя из БД"):
            #Удаляем
            self.db.delete(max_id)