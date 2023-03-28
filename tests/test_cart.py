import allure
from selene.support.shared import browser


from components.staya import header_menu, cart_rightside_menu
from pages.staya_dog import main_page, product_page, catalog_page, checkout_page

@allure.parent_suite("Web")
@allure.suite("Cart")
@allure.title("Adding a product to cart")
def test_add_to_cart(setup_browser):
    main_page.open_main_page()

    with allure.step('Перейти в каталог'):
        header_menu.choose_section("Каталог")

    with allure.step('Выбрать случайный товар'):
        catalog_page.choose_products_in_stock()
        catalog_page.choose_random_product()
        product_page.remember_product()

    with allure.step('Выбрать размер'):
        product_page.select_size()

    with allure.step('Добавить в корзину'):
        product_page.add_to_cart()

    with allure.step('Перейти в корзину'):
        cart_rightside_menu.submit_checkout()

    with allure.step('Проверить что в корзине лежит добавленный товар'):
        checkout_page.assert_product_in_cart()

@allure.parent_suite("Web")
@allure.suite("Cart")
@allure.title("Clearing a cart")
def test_clear_cart(setup_browser):
    main_page.open_main_page()
    with allure.step('Открыть меню корзины'):
        header_menu.open_cart()
    with allure.step('Перейти в корзину'):
        cart_rightside_menu.submit_checkout()
    with allure.step('Очистить корзину'):
        checkout_page.clear_the_cart()
    with allure.step('Проверить, что корзина пустая'):
        checkout_page.assert_the_cart_is_emply()


