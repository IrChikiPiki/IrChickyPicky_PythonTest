from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс главной страницы сайта калькулятора"""

    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-"
            "java/slow-calculator.html"
        )
        self.driver.maximize_window()

    def set_delay(self):
        """Устанавливаем задержку"""
        action = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        action.clear()
        action.send_keys(f"{self.delay}")

    def set_key(self, key):
        """Кликаем по выбранной кнопке"""
        self.driver.find_element(By.XPATH, f"//span[text()='{key}']").click()

    def get_result(self):
        """Получаем результат с учётом задержки"""
        WebDriverWait(self.driver, self.delay + 1).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "span#spinner")
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
