from pages.shop_pages import LoginShopPage, MainPage, CartPage, OrderPage


def test_shop_purchase(driver_Chrome):
    """Проверка работы подсчёта суммы покупки"""

    # Открываем страницу
    login_page = LoginShopPage(driver_Chrome)
    login_page.login()

    # Работаем с основной страницей
    main_page = MainPage(driver_Chrome)
    main_page.add_to_cart()
    main_page.go_to_shop_cart()

    # Работаем с корзиной
    cart_page = CartPage(driver_Chrome)
    item_list = cart_page.check_cart()
    print(item_list)
    cart_page.click_checkout()

    # Оформляем заказ
    order_page = OrderPage(driver_Chrome)
    order_page.fill_out_data("Oleg", "Olegov", "1212")
    order_page.click_continue()
    total_sum = order_page.get_total_purchase()
    assert total_sum == "$58.29"
