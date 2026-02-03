import pytest
from selenium import webdriver
from pages.main_page import CalcMainPage

# Фикстура для драйвера Chrome
@pytest.fixture()
def driver():
  driver = webdriver.Chrome()
  yield driver
  driver.quit()

def test_calc_result(driver):
    """Проверка корректного ответа калькулятора"""
    # Выбираем необходимую задержку
    delay = 45

    # Открываем страницу
    calc_page = CalcMainPage(driver, delay)

    # Устанавливаем задержку
    calc_page.set_delay()

    # Кликаем по калькулятору
    calc_page.set_key(7)
    calc_page.set_key("+")
    calc_page.set_key(8)
    calc_page.set_key('=')

    # Получаем результат
    result = calc_page.get_result()

    # Сравниваем
    assert result == "15"

