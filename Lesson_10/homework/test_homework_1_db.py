from HomeWorkApi import HomeWorkApi
from HomeWorkDb import HomeWorkDb

api = HomeWorkApi("http://5.101.50.27:8000")
db = HomeWorkDb("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

# [GET] /employee
def test_get_employee_id():
    test_id=1
    result = db.get_employee_by_id(test_id)
    get_emloyee_id = result
    assert get_emloyee_id["company_id"] == test_id


# [POST] /employee
def test_create_employee():
    fist_name="Иван"
    last_name="Иванов"
    middle_name="Иванович"
    company_id = 1
    email="user@example.com"
    phone="+78005553535"
    birthdate="2025-01-01"
    is_active=True

    db.create(first_name=fist_name, last_name=last_name, middle_name=middle_name, company_id=company_id, email=email, phone=phone, birthdate=birthdate, is_active=is_active)

    max_id = db.get_max_id()

    last_employee = api.obtaining_employee_data_by_ID(max_id)

    get_create_employee = last_employee

    assert get_create_employee["first_name"] == "Иван"
    assert get_create_employee["last_name"] == "Иванов"
    assert get_create_employee["middle_name"] == "Иванович"
    assert get_create_employee["company_id"] == 1
    assert get_create_employee["email"] == "user@example.com"
    assert get_create_employee["phone"] == "+78005553535"
    assert get_create_employee["birthdate"] == "2025-01-01"
    assert get_create_employee["is_active"] == True
    assert len(get_create_employee) == 8

    db.delete(max_id)


# [GET] /employee/{id}
def test_get_employee_id_list():
    test_id=1
    result = db.get_employee_by_id_list(test_id)
    get_emloyee_id = result
    assert get_emloyee_id[-1]["company_id"] == test_id
    assert len(get_emloyee_id[-1]) == 11


# [PATCH] /employee/{id}
def test_change_employee():
    #Создаем
    fist_name="Иван"
    last_name="Иванов"
    middle_name="Иванович"
    company_id = 1
    email="user@example.com"
    phone="+78005553535"
    birthdate="2025-01-01"
    is_active=True

    db.create(first_name=fist_name, last_name=last_name, middle_name=middle_name, company_id=company_id, email=email, phone=phone, birthdate=birthdate, is_active=is_active)

    max_id = db.get_max_id()

    #Редактируем
    employee_id = max_id
    last_name = "Ивашка"
    email = "dfdfd@example.com"
    phone = "+79995553535"
    result = api.change_company_id_employee(employee_id, last_name, email, phone, True)
    get_change_employee = result
    assert get_change_employee["last_name"] == "Ивашка"
    assert get_change_employee["email"] == "dfdfd@example.com"
    assert get_change_employee["phone"] == "+79995553535"
    assert get_change_employee["is_active"] == True
    assert len(get_change_employee) == 8

    #Удаляем
    db.delete(max_id)