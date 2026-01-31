from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Регистрируем драйвер для Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Заходим на страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ищем элементы и взаимодействуем с ними
input_form = driver.find_element(By.CSS_SELECTOR, "input#username")
input_form.send_keys("tomsmith")

input_form = driver.find_element(By.CSS_SELECTOR, "input#password")
input_form.send_keys("SuperSecretPassword!")
sleep(3)

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

text_field = driver.find_element(By.CSS_SELECTOR, "#flash")
print(text_field.text)

# Завершаем работу
driver.quit()
