from selenium import webdriver
from selenium.webdriver.common.by import By

# Регистрируем драйвер для Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Заходим на страницу
driver.get("https://www.saucedemo.com/")


# Авторизуемся
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

# Добавляем товары в корзину
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
).click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
).click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

# Переходим в корзину
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

# Нажимаем чекаут
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# Заполняем данные

first_name = "Oleg"
last_name = "Olegov"
zip_code = "1212"

driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)
driver.find_element(By.CSS_SELECTOR, "#continue").click()

# Получаем текст с суммой
total = driver.find_element(
    By.CSS_SELECTOR, 'div[data-test="total-label"]'
).text

# Делим на слова
words = total.split()

# Закрываем драйвер
driver.quit()


def test_total_purchase():
    assert words[1] == "$58.29"
