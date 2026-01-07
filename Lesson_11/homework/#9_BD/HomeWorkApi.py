import requests
import allure


class HomeWorkApi:
    # Инициализация
    def __init__(self, url) -> None:
        '''
        Конструктор url
        '''
        self.url = url

    @allure.step("api. Получение токена пользователя {user}:{password}")
    def get_token(self, user: str='harrypotter', password: str='expelliarmus') -> dict:
        '''
        Получение токена пользователя
        '''
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]
    
    
    # [POST] /employee
    @allure.step("api. Создание пользователя {fist_name}:{last_name}:{middle_name}:{company_id}:{email}:{phone}:{birthdate} -> {is_active}")
    def create_employee(self, fist_name: str="Иван", last_name: str="Иванов", middle_name: str="Иванович", company_id: str="",email: str="user@example.com", phone: str="+78005553535",birthdate: str="2025-11-20",is_active: bool=True) -> dict:
        '''
        Создание пользователя
        '''
        employee = {
            "first_name": fist_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }
        resp = requests.post(self.url + '/employee/create', json=employee)
        return resp.json()
    

    # [GET] /employee
    @allure.step("api. Получение пользователя по {id}")
    def get_employee_by_id(self, id: int) -> dict:
        '''
        Получение пользователя по id
        '''
        resp = requests.get(self.url + '/employee/info/' + str(id))
        return resp.json()
    
    @allure.step("api. Поиск последнего пользователя в диапазоне {start_id}:{end_id}")
    def find_last_employee_id(self, start_id: int=1, end_id: int=100) -> int:
        '''
        Поиск пгоследнего пользователя в диапазоне
        '''
        last_id = 0
        
        for employee_id in range(start_id, end_id + 1):
            try:
                employee_data = self.get_employee_by_id(employee_id)
                if employee_data and 'error' not in employee_data:
                    last_id = max(last_id, employee_id)
            except Exception:
                continue
        
        return last_id
    

    # [GET] /employee/{id}  
    @allure.step("api. Получение пользователей из списка по {id}")
    def get_employees_by_company_id(self, id: int) -> dict:
        '''
        Получение пользователей из списка по id
        '''
        resp = requests.get(self.url + '/employee/list/' + str(id))
        return resp.json()
    

    # [PATCH] /employee/{id}
    @allure.step("api. Изменение компании по {id} пользователя {last_name}:{email}:{phone} -> {is_active}")
    def change_company_id_employee(self, id: int, last_name: str="Ивашка", email: str="dfdfd@example.com", phone: str="+79995553535", is_active: bool=True) -> dict:
        '''
        Измнение компании по id пользователя.
        '''
        token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{id}?client_token={token}"
        employee = {
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "is_active": is_active
        }
        resp = requests.patch(url_with_token, json=employee)
        return resp.json()