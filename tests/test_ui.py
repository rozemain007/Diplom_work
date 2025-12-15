import allure
from selenium import webdriver
from pages.method_ui import UImethods
from config import MAIN_PAGE_URL


@allure.title("Поиск товара - валидное значение")
def test_search_val():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    with allure.step("Перейти на страницу поиска"):
        browser.go_to_main_page(MAIN_PAGE_URL)
    with allure.step("Ввести поисковый запрос"):
        search_phrase = "Python"
        browser.send_search_str(search_phrase)
    with allure.step("Получить название первой кнги"):
        text = browser.get_founded_book()
    with allure.step("Сравнить есть ли слово-запрос в названии"):
        assert search_phrase in text
    driver.quit()


@allure.title("Поиск товара - числа")
def test_search_num():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    with allure.step("Перейти на страницу поиска"):
        browser.go_to_main_page(MAIN_PAGE_URL)
    with allure.step("Ввести поисковый запрос"):
        search_phrase = "123456789"
        browser.send_search_str(search_phrase)
    with allure.step("Получить ответ 'Похоже, у нас такого нет"):
        text = browser.not_founded()
    with allure.step("Сравнить, соответсвует ли результат ожидаемому"):
        assert text == "Похоже, у нас такого нет"
    driver.quit()


@allure.title("Поиск товара - спец.символы в запросе")
def test_search_simbols():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    with allure.step("Перейти на страницу поиска"):
        browser.go_to_main_page(MAIN_PAGE_URL)
    with allure.step("Ввести поисковый запрос"):
        search_phrase = "저는 과제를 제출하고 싶습니다."
        browser.send_search_str(search_phrase)
    with allure.step("Получить ответ 'Похоже, у нас такого нет"):
        text = browser.not_founded()
    with allure.step("Сравнить, соответствует ли результат ожидаемому"):
        assert text == "Похоже, у нас такого нет"
    driver.quit()


@allure.title("Добавление товара в корзину")
def test_add_to_basket():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    with allure.step("Перейти на страницу поиска"):
        browser.go_to_main_page(MAIN_PAGE_URL)
    with allure.step("Ввести поисковый запрос"):
        search_phrase = "Python"
        browser.send_search_str(search_phrase)
    with allure.step("Добавить книгу в корзину"):
        browser.add_book()
    with allure.step("Получить кол-во товаров в корзине"):
        items = browser.busket()
    with allure.step("Сравнить полученное кол-во с ожидаемым"):
        assert items == "1 товар"
    driver.quit()


@allure.title("Удаление товара из корзины")
def test_remove_book():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    with allure.step("Перейти на страницу поиска"):
        browser.go_to_main_page(MAIN_PAGE_URL)
    with allure.step("Ввести поисковый запрос"):
        search_phrase = "Пайтон"
        browser.send_search_str(search_phrase)
    with allure.step('Добавить книгу в корзину'):
        browser.add_book()
    with allure.step("Удалить книгу из корзины"):
        browser.remove_item()
    with allure.step("Получить кол-во товаров в корзине"):
        no_found = browser.no_found()
    with allure.step("Убедиться что корзина пуста"):
        assert no_found == "В корзине ничего нет"
    driver.quit()
