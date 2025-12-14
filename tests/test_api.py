import allure
from pages.method_api import API
from config import API_URL, TOKEN


api_object = API(API_URL)


@allure.title("Поиск введен кириллицей")
def test_search_kir():
    with allure.step("Отправляем запрос кириллицей и получаем status_code"):
        search = api_object.search(TOKEN, "Читай")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search.status_code == 200


@allure.title('Поиск введен латиницей')
def test_search_lat():
    with allure.step("Отправляем запрос латиницей и получаем status_code"):
        search = api_object.search(TOKEN, "Read")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search.status_code == 200


@allure.title("Поиск введен цифрами")
def test_search_int():
    with allure.step("Отправляем запрос цифрами и получаем status_code"):
        search = api_object.search(TOKEN, "12122025")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search.status_code == 200


@allure.title("Поиск без авторизации")
def test_no_auth():
    with allure.step("Отправляем запрос без токена авторизации"):
        search = api_object.search("", "Search")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search.status_code == 401


@allure.title("Поиск с пустым запросом")
def test_none_str():
    with allure.step("Отправляем пустой запрос"):
        search = api_object.search(TOKEN,"")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search.status_code == 422