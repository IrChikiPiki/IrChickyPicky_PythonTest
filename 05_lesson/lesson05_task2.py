from selenium import webdriver
from selenium.webdriver.common.by import By

# Регистрируем драйвер для Firefox
driver = webdriver.Chrome()
driver.maximize_window()

# Заходим на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Ищем элемент и взаимодействуем с ним
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()
