from selenium import webdriver
from selenium.webdriver.common.by import By

# Регистрируем драйвер для Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Заходим на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Ищем элемент и взаимодействуем с ним
input_form = driver.find_element(By.CSS_SELECTOR, "input")
input_form.send_keys("Sky")
input_form.clear()
input_form.send_keys("Pro")

# Завершаем работу
driver.quit()
