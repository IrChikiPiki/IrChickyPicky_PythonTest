from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Регистрируем драйвер для Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Заходим на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Настраиваем вэйтер
waiter = WebDriverWait(driver, 40)

# Ждём загрузки картинок и появления сообщения об окончании загрузки
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!"))

# Определяем все загруженные картинки
image_container = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

# Выводим src у третьей картинки
print(image_container[2].get_attribute("src"))

# Закрываем драйвер
driver.quit()
