import requests


base_url = "http://5.101.50.27:8000"

def test_get_companies():
    resp = requests.get(base_url+'/company/list')
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0


def test_get_active_companies():
    # Получить список всех компаний
    resp = requests.get(base_url+'/company/list')
    full_list = resp.json()

    # Получить список активных компаний
    resp = requests.get(base_url+'/company/list?active=true')
    filtered_list = resp.json()

    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)


# def test_get_active_companies():
#     # Получить список всех компаний
#     resp = requests.get(base_url+'/company/list')
#     full_list = resp.json()

    # # Получить список активных компаний
    # my_params = {'active' : 'true'}
    # resp = requests.get(base_url+'/company/list', params=my_params)
    # filtered_list = resp.json()

#     # Проверить, что список 1 > списка 2
#     assert len(full_list) > len(filtered_list)


# def test_get_active_companies():
#     # Получить список всех компаний
#     resp = requests.get(base_url+'/company/list')
#     full_list = resp.json()

    # # Получить список активных компаний
    # resp = requests.get(base_url+'/company/list', params={'active' : 'true'})
    # filtered_list = resp.json()

#     # Проверить, что список 1 > списка 2
#     assert len(full_list) > len(filtered_list)


def get_company_list(params_to_add = None):
        resp = requests.get(base_url+'/company/list', params_to_add)
        return resp.json()


def get_token(user = 'harrypotter', password = 'expelliarmus'):
    creds = {
        'username': user,
        'password': password
        }
    resp = requests.post(base_url+'/auth/login', json=creds)
    return resp.json()["user_token"]


def create_company(name, description=""):
    company = {
            "name": name,
            "description": description
     }
    resp = requests.post(base_url + '/company/create',
                             json=company)
    return resp.json()


def test_add_new():
    # Получить количество компаний до
    body = get_company_list()
    len_before = len(body) # Находим длину переменной

    # Создать новую компанию
    name = "Autotest"
    descr = "Descr"
    create_company(name, descr)

    # Получить количество компаний после
    body = get_company_list()
    len_after = len(body) # Находим длину переменной

    # Проверить, что размер списка увеличен на +1
    assert len_after - len_before == 1
    # Проверить название и описание
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr