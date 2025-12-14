from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class UImethods:

    def __init__(self, driver):
        self.driver = driver

    def go_to_main_page(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        self.close_popups()

    def close_popups(self):
        """
        Закрывает все всплывающие окна безопасно (без падения теста)
        """
        popup_selectors = [
            ('.chg-app-button--primary.chg-app-button--block', 3),
            ('[data-popmechanic-close]', 3)
        ]

        for selector, timeout in popup_selectors:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()

                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, selector))
                )
            except TimeoutException:
                continue

    def send_search_str(self, search_str: str):
        """
        Поиск по ключевым словам
        """
        button = self.driver.find_element(By.NAME, "search")
        button.send_keys(search_str)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.text_to_be_present_in_element_attribute((By.NAME, "search"), "value", search_str))
        self.driver.implicitly_wait(10)
        button.send_keys(Keys.RETURN)

    def get_founded_book(self):
        """
        Находим первый элемент поиска
        """
        wait = WebDriverWait(self.driver, 20)
        search_page_loc = (By.CSS_SELECTOR, "h1.search-title__head")
        wait.until(EC.presence_of_element_located(search_page_loc))

        title = self.driver.find_element(By.CSS_SELECTOR, 'a.product-card__title')
        text_title = title.text
        return text_title

    def not_founded(self) -> str:
        wait = WebDriverWait(self.driver, 20)
        not_found_locator = (By.CSS_SELECTOR, 'h4.catalog-stub__title')
        wait.until(EC.presence_of_element_located(not_found_locator))

        not_found = self.driver.find_element(By.CSS_SELECTOR, 'h4.catalog-stub__title')
        text = not_found.text
        return text

    def add_book(self):
        """
        Добавление в корзину
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.search-title__head")))

        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollBy(0, 800);")

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-buttons.product-card__actions")))
        self.driver.find_element(By.CSS_SELECTOR, 'div.product-buttons.product-card__actions').click()

    def busket(self) -> str:
        self.driver.get("https://www.chitai-gorod.ru/cart")
        count_items = self.driver.find_element(By.CSS_SELECTOR, "div.info-item__title").text
        text = f"{count_items}"
        return text

    def remove_item(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.cart-item__delete-button").click()
        self.driver.refresh()

    def no_found(self) -> str:
        no_found = self.driver.find_element(By.CSS_SELECTOR, "h4.catalog-stub__title")
        text_no_found = no_found.text
        return text_no_found
