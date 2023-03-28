import allure
# from components.staya_dog import header_menu, cart_rightside_menu
# from pages.staya_dog import main_page, product_page, catalog_page, checkout_page
from app import app

@allure.parent_suite("Web")
@allure.suite("Cart")
@allure.title("Adding a product to cart")
def test_add_to_cart(setup_browser):
    app.main.open_main_page()

    with allure.step('Перейти в каталог'):
        app.header_menu.choose_section("Каталог")

    with allure.step('Выбрать случайный товар'):
        app.catalog.choose_products_in_stock()
        app.catalog.choose_random_product()
        app.product.remember_product()

    with allure.step('Выбрать размер'):
        app.product.select_size()

    with allure.step('Добавить в корзину'):
        app.product.add_to_cart()

    with allure.step('Перейти в корзину'):
        app.rightside_cart.submit_checkout()

    with allure.step('Проверить что в корзине лежит добавленный товар'):
        app.checkout.assert_product_in_cart()


@allure.parent_suite("Web")
@allure.suite("Cart")
@allure.title("Clearing a cart")
def test_clear_cart(setup_browser):
    app.main.open_main_page()
    with allure.step('Открыть меню корзины'):
        app.header_menu.open_cart()
    with allure.step('Перейти в корзину'):
        app.rightside_cart.submit_checkout()
    with allure.step('Очистить корзину'):
        app.checkout.clear_the_cart()
    with allure.step('Проверить, что корзина пустая'):
        app.checkout.assert_the_cart_is_emply()
