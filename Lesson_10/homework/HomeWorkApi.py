import requests


class HomeWorkApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url


    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]
    
    
    # [POST] /employee

    def create_employee(self, fist_name="Иван", last_name="Иванов", middle_name="Иванович", company_id="",email="user@example.com", phone="+78005553535",birthdate="2025-11-20",is_active=True):
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

    def obtaining_employee_data_by_ID(self, id):
        resp = requests.get(self.url + '/employee/info/' + str(id))
        return resp.json()
    

    def find_last_employee_id(self, start_id=1, end_id=100):
        last_id = 0
        
        for employee_id in range(start_id, end_id + 1):
            try:
                employee_data = self.obtaining_employee_data_by_ID(employee_id)
                if employee_data and 'error' not in employee_data:
                    last_id = max(last_id, employee_id)
            except Exception:
                continue
        
        return last_id
    

    # [GET] /employee/{id}
    def get_company_id_employee(self, id):
        resp = requests.get(self.url + '/employee/list/' + str(id))
        return resp.json()
    

    # [PATCH] /employee/{id}
    def change_company_id_employee(self, id, last_name="Ивашка", email="dfdfd@example.com", phone="+79995553535", is_active=True):
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