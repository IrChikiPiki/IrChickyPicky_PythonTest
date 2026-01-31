from selenium import webdriver
from selenium.webdriver.common.by import By

# Регистрируем драйвер для Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Заходим на страницу
driver.get("http://uitestingplayground.com/textinput")

# Вводим текст в форму
name_form = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# Нажимаем на синюю кнопку и выводим подпись
blue_btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_btn.click()

print(blue_btn.text)

# Закрываем драйвер
driver.quit()
