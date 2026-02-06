import requests


class YouGileAPI:
    """Класс для работы с API YouGile"""

    def __init__(self, url):
        self.url = url

    def create_bearer_token(self, login, password, companyId):
        """
        Создание токена авторизации
        Аттрибуты:
        login: логин от аккаунта в YouGile
        password: пароль от аккаунта в YouGile
        companyId: id компании в YouGile
        Возвращает токен аторизации
        """

        auth = dict()
        auth["login"] = login
        auth["password"] = password
        auth["companyId"] = companyId
        resp = requests.post(self.url + "auth/keys", auth)
        return resp.json().get("key")

    def get_bearer_token(self, login, password, companyId):
        """
        Получение списка токенов авторизации
        Аттрибуты:
        login: логин от аккаунта в YouGile
        password: пароль от аккаунта в YouGile
        companyId: id компании в YouGile
        Возвращает токен аторизации
        """

        auth = dict()
        auth["login"] = login
        auth["password"] = password
        auth["companyId"] = companyId
        resp = requests.post(self.url + "auth/keys/get", auth).json()
        return resp

    def create_project(self, project_name, token):
        """
        Создание проекта
        Аттрибуты:
        project_name: название нового проекта в YouGile
        token: токен авторизации в YouGile
        Возвращает id проекта
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        payload = {
            "title": project_name,
        }
        new_project = requests.post(
            self.url + "projects", json=payload, headers=headers
        )
        return new_project

    def get_project(self, project_id, token):
        """
        Получение данных проекта
        Аттрибуты:
        project_id: id проекта в YouGile
        token: токен авторизации в YouGile
        Возвращает данные проекта
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        resp = requests.get(
            self.url + f"projects/{project_id}", headers=headers
        )
        return resp

    def get_projects(self, token):
        """
        Получение списка проектов
        Аттрибуты:
        token: токен авторизации в YouGile
        Возвращает данные проектов
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        resp = requests.get(self.url + "projects", headers=headers)
        return resp

    def change_project(
        self, project_id, token, title="Пример проекта", deleted=False
    ):
        """
        Изменение данных проекта
        Аттрибуты:
        project_id: id проекта в YouGile
        token: токен авторизации в YouGile
        title: имя проекта
        deleted: статус удаления
        Возвращает данные проекта
        """
        payload = {
            "deleted": False,
            "title": title,
            "users": {
                "1678c8b9-fb6b-4dee-bea8-e151d239542f": "admin",
            },
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        resp = requests.put(
            self.url + f"projects/{project_id}", json=payload, headers=headers
        )
        return resp
