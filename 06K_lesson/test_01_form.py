from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Регистрируем драйвер для Firefox
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(15)


# Заходим на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Вводим текст в формы
form = driver.find_elements(By.CSS_SELECTOR, "input.form-control")
form[0].send_keys("Иван")
form[1].send_keys("Петров")
form[2].send_keys("Ленина, 55-3")
form[4].send_keys("Россия")
form[5].send_keys("Москва")
form[6].send_keys("test@skypro.com")
form[7].send_keys("+7985899998787")
form[8].send_keys("QA")
form[9].send_keys("SkyPro")

# Нажимаем на синюю кнопку и выводим подпись
blue_btn = driver.find_element(By.CSS_SELECTOR, "button").click()

# Получаем значение класса у поля zip-code
zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")

# Формируем список id остальных полей для локатора
list_id = [
    "#first-name",
    "#last-name",
    "#address",
    "#city",
    "#country",
    "#e-mail",
    "#phone",
    "#job-position",
    "#company",
]


list_classes = []
for i in list_id:
    class_element = driver.find_element(By.CSS_SELECTOR, i).get_attribute("class")
    list_classes.append(class_element)

# Закрываем драйвер
driver.quit()


def test_zip_code():
    """Тест проверки zip-code на соответствие класса красного цвета"""
    assert zip_code == "alert py-2 alert-danger"


def test_other_elements():
    """Тест проверки остальных полей на соответствие класса зелёного цвета"""
    for element in list_classes:
        assert element == "alert py-2 alert-success"
