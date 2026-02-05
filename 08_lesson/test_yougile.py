from yougileAPI import YouGileAPI
import os
from dotenv import load_dotenv

load_dotenv()


base_url = "https://ru.yougile.com/api-v2/"
login = os.getenv("login")
password = os.getenv("password")
companyId = "83922095-5c06-46b0-a192-0b50073ced49"
api = YouGileAPI(base_url)

keys = api.get_bearer_token(login, password, companyId)
if len(keys) > 0:
    key = keys[0].get("key")
else:
    key = api.create_bearer_token(login, password, companyId)


def test_create_project_positive():
    """Тест создания проекта"""
    new_project = api.create_project("TEST_new", key)
    assert "id" in new_project.json()
    assert new_project.status_code == 201


def test_create_project_negative():
    """Тест создания проекта с неправильным токеном"""
    new_project = api.create_project("TEST_new", "12341234")
    assert new_project.status_code == 401


def test_get_project_positive():
    """Тест просмотра данных проекта"""
    projects = api.get_projects(key)
    if len(projects.json()) > 0:
        project_inf = projects.json()
        project_id = project_inf.get("content")[0].get("id")
        project = api.get_project(project_id, key)
        assert project.status_code == 200
        assert project.json()["id"] == project_id
    else:
        print("Проекты не созданы! Создайте новый.")


def test_get_project_negative():
    """Тест просмотра данных проекта с неправильным id проекта"""
    projects = api.get_projects(key)
    if len(projects.json()) > 0:
        project = api.get_project("1234", key)
        assert project.status_code == 404
    else:
        print("Проекты не созданы! Создайте новый.")


def test_change_project_positive():
    """Тест изменения данных проекта"""
    projects = api.get_projects(key)
    if len(projects.json()) > 0:
        project_inf = projects.json()
        project_id = project_inf.get("content")[0].get("id")
        project = api.change_project(project_id, key, title="NEW TEST3")
        assert project.status_code == 200
        assert project.json()["id"] == project_id
    else:
        print("Проекты не созданы! Создайте новый.")


def test_change_project_negative():
    """Тест изменения данных проекта с неправильным токеном"""
    projects = api.get_projects(key)
    if len(projects.json()) > 0:
        project_inf = projects.json()
        project_id = project_inf.get("content")[0].get("id")
        project = api.change_project(project_id, "123", title="NEW TEST3")
        assert project.status_code == 401
    else:
        print("Проекты не созданы! Создайте новый.")
