from selenium.webdriver.common.by import By


class LoginShopPage:
    """Класс главной страницы магазина одежды"""

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def login(self):
        """Метод авторизации пользователя"""
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
            "standard_user"
        )
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
            "secret_sauce"
        )
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()


class MainPage:
    """Класс страницы с карточками товаров магазина одежды"""

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        """Метод добавления товаров в корзину"""
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()

    def go_to_shop_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
        ).click()


class CartPage:
    """Класс страницы корзины товаров магазина одежды"""

    def __init__(self, driver):
        self.driver = driver

    def check_cart(self):
        """Метод проверки содержимого корзины"""
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_name"
        )
        item_list = []
        for el in elements:
            item_list.append(el.text)
        return item_list

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()


class OrderPage:
    """Класс страницы корзины товаров магазина одежды"""

    def __init__(self, driver):
        self.driver = driver

    def fill_out_data(self, first_name, last_name, zip_code):
        """Метод заполнения данных для отправки"""
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(
            first_name
        )
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(
            last_name
        )
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(
            zip_code
        )

    def click_continue(self):
        """Переход на итоговую страницу заказа"""
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total_purchase(self):
        """Получени итоговой стоимости заказа"""
        total = self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-test="total-label"]'
        ).text
        words = total.split()
        return words[1]
