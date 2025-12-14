import allure
from selenium import webdriver
from pages.method_ui import UImethods


@allure.title("Поиск товара - валидное значение")
def test_search_val():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    search_phrase = "Python"
    browser.send_search_str(search_phrase)
    text = browser.get_founded_book()
    assert search_phrase in text
    driver.quit()


@allure.title("Поиск товара - числа")
def test_search_num():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    search_phrase = "123456789"
    browser.send_search_str(search_phrase)
    text = browser.not_founded()
    assert text == "Похоже, у нас такого нет"
    driver.quit()


@allure.title("Поиск товара - спец.символы в запросе")
def test_search_simbols():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    search_phrase = "저는 과제를 제출하고 싶습니다."
    browser.send_search_str(search_phrase)
    text = browser.not_founded()
    assert text == "Похоже, у нас такого нет"
    driver.quit()


@allure.title("Добавление товара в корзину")
def test_add_to_basket():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    search_phrase = "Python"
    browser.send_search_str(search_phrase)
    browser.add_book()
    items = browser.busket()
    assert items == "1 товар"
    driver.quit()


@allure.title("Удаление товара из корзины")
def test_remove_book():
    driver = webdriver.Chrome()
    browser = UImethods(driver)
    search_phrase = "Пайтон"
    browser.send_search_str(search_phrase)
    browser.add_book()
    browser.remove_item()
    no_found = browser.no_found()
    assert no_found == "В корзине ничего нет"
