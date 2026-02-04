from pages.calculator_page import CalculatorPage


def test_calc_result(driver_Firefox):
    """Проверка корректного ответа калькулятора"""
    # Выбираем необходимую задержку
    delay = 45

    # Открываем страницу
    calc_page = CalculatorPage(driver_Firefox, delay)

    # Устанавливаем задержку
    calc_page.set_delay()

    # Кликаем по калькулятору
    calc_page.set_key(7)
    calc_page.set_key("+")
    calc_page.set_key(8)
    calc_page.set_key("=")

    # Получаем результат
    result = calc_page.get_result()

    # Сравниваем
    assert result == "15"
