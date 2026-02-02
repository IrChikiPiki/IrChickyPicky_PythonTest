from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Регистрируем драйвер для Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Заходим на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
waiter = WebDriverWait(driver, 45)

# Ищем элементы и взаимодействуем с ним
delay_form = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_form.clear()
delay_form.send_keys("45")

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
result = driver.find_element(By.CSS_SELECTOR, ".screen").text


# Закрываем драйвер
driver.quit()


def test_calc_result():
    """Проверка корректного ответа калькулятора"""
    assert result == "15"
