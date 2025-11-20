import requests


class HomeworkAPI2:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # Получение списка.
    def get_todo_list(self):
        resp = requests.get(self.url)
        return resp.json()
    
    # Создание
    def create_todo_list(self, title, completed=False):
        title = {
            "title": title,
            "completed": completed
        }
        resp = requests.post(self.url, json=title)
        return resp.json()
    
    # Переименование.
    def rename_todo_list(self, id, title, completed=False):
        title = {
            "title": title,
            "completed": completed
        }
        resp = requests.patch(self.url + id, json=title)
        return resp.json()
    
    # Удаление
    def deleted_todo_list(self, id):
        resp = requests.delete(self.url + id)
        return resp.json()
    
    # Получение конкретной задачи из списка.
    def get_id_todo_list(self, id):
        resp = requests.get(self.url + id)
        return resp.json()
    
    # Отметка задачи «Выполнена».
    def completed_todo_list(self, id, completed=True):
        title = {
            "completed": completed
        }
        resp = requests.patch(self.url + id, json=title)
        return resp.json()
    
    # Снятие отметки «Выполнена».
    def uncompleted_todo_list(self, id, completed=False):
        title = {
            "completed": completed
        }
        resp = requests.patch(self.url + id, json=title)
        return resp.json()