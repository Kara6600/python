import requests
import pytest

# Базовый URL
BASE_URL = "https://yougile.com"

# Переменная для хранения API-ключа
API_TOKEN = None

# Функция получения API-ключа
def obtain_api_token():
    url = "http://localhost:8001/api-v2/auth/keys"  # или другой URL для локальной среды
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "login": "dev@yougile.com",
        "password": "123",
        "companyId": "44eccf40-a027-4d06-b5c2-18f4c02bb026"
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    return result["apiKey"]  # Предположим, ответ содержит это поле

# Получение токена перед запуском тестов
@pytest.fixture(scope="session", autouse=True)
def setup_token():
    global API_TOKEN
    API_TOKEN = obtain_api_token()

# Обновляем headers каждый раз, берём токен из переменной
@pytest.fixture
def get_headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

# Используем фикстуру get_headers в тестах
def create_project(get_headers):
    url = f"{BASE_URL}/api-v2/projects"
    payload = {
        "name": "Test Project"
        # добавьте обязательные поля по документации
    }
    response = requests.post(url, headers=get_headers, json=payload)
    response.raise_for_status()
    return response.json()["id"]

def delete_project(project_id, get_headers):
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    requests.delete(url, headers=get_headers)

@pytest.fixture(scope="module")
def project_id(get_headers):
    pid = create_project(get_headers)
    yield pid
    delete_project(pid, get_headers)

def test_get_project_positive(project_id, get_headers):
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    response = requests.get(url, headers=get_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id

def test_get_project_negative(get_headers):
    url = f"{BASE_URL}/api-v2/projects/invalid_id"
    response = requests.get(url, headers=get_headers)
    assert response.status_code == 404

def test_update_project_positive(project_id, get_headers):
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    payload = {
        "name": "Updated Project Name"
        # добавьте другие поля по необходимости
    }
    response = requests.put(url, headers=get_headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Project Name"

def test_update_project_negative(get_headers):
    url = f"{BASE_URL}/api-v2/projects/invalid_id"
    payload = {
        "name": "Should Fail"
    }
    response = requests.put(url, headers=get_headers, json=payload)
    assert response.status_code == 404

def test_create_project_positive(get_headers):
    url = f"{BASE_URL}/api-v2/projects"
    payload = {
        "name": "New Test Project"
        # добавьте другие обязательные поля по документации
    }
    response = requests.post(url, headers=get_headers, json=payload)
    assert response.status_code == 201
    data = response.json()
    # проверка создания
    assert data["name"] == "New Test Project"
    # удаляем созданный проект
    delete_project(data["id"], get_headers)

def test_create_project_negative(get_headers):
    url = f"{BASE_URL}/api-v2/projects"
    payload = {
        # пропущенные обязательные поля или некорректный формат
    }
    response = requests.post(url, headers=get_headers, json=payload)
    assert response.status_code == 400