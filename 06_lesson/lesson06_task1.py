from selenium import webdriver
from selenium.webdriver.common.by import By

# Регистрируем драйвер для Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Заходим на страницу
driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(16)

# Нажимаем на синюю кнопку
blue_btn = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получаем и выводим текст
green_form = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(green_form)

# Закрываем драйвер
driver.quit()
