from HomeWorkApi import HomeWorkApi

api = HomeWorkApi("http://5.101.50.27:8000")

# [GET] /employee
def test_get_employee_id():
    test_id=1
    result = api.obtaining_employee_data_by_ID(test_id)
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

    api.create_employee(fist_name,last_name,middle_name,company_id,email,phone,birthdate,is_active)

    last_id = api.find_last_employee_id()

    last_employee = api.obtaining_employee_data_by_ID(last_id)

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


# [GET] /employee/{id}
def test_get_company_id():
    test_id=1
    result = api.get_company_id_employee(test_id)
    get_emloyee_id = result
    assert get_emloyee_id[-1]["company_id"] == test_id
    assert len(get_emloyee_id[-1]) == 8


# [PATCH] /employee/{id}
def test_change_employee():
    employee_id = 16
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