import allure
from app import app
from allure_commons.types import Severity


class TestAddToCart:
    @allure.parent_suite("Web")
    @allure.severity(Severity.NORMAL)
    @allure.suite("Cart")
    @allure.title("Adding a product to cart")
    def test_add_to_cart(self):
        app.base.open_main_page()

        with allure.step('Перейти в каталог'):
            app.header_menu.choose_section("Каталог")

        with allure.step('Выбрать случайный товар'):
            app.catalog.choose_products_in_stock()
            app.catalog.choose_random_product()
            collection_name, article_name = app.product.remember_product()

        with allure.step('Выбрать размер'):
            app.product.select_size()

        with allure.step('Добавить в корзину'):
            app.product.add_to_cart()

        with allure.step('Перейти в корзину'):
            app.rightside_cart.submit_checkout()

        with allure.step('Проверить что в корзине лежит добавленный товар'):
            app.checkout.assert_product_in_cart(collection_name, article_name)


class TestClearCart:
    @classmethod
    def setup_class(cls):
        app.base.open_main_page()

        with allure.step('Добавление товара в корзину'):
            app.header_menu.choose_section("Каталог")

            app.catalog.choose_products_in_stock()
            app.catalog.choose_random_product()

            app.product.select_size()

            app.product.add_to_cart()

            app.rightside_cart.submit_checkout()

            app.base.open_main_page()

    @allure.parent_suite("Web")
    @allure.severity(Severity.NORMAL)
    @allure.suite("Cart")
    @allure.title("Clearing a cart")
    def test_clear_cart(self):
        with allure.step('Открыть меню корзины'):
            app.header_menu.open_cart()
        with allure.step('Перейти в корзину'):
            app.rightside_cart.submit_checkout()

        with allure.step('Очистить корзину'):
            app.checkout.clear_the_cart()
        with allure.step('Проверить, что корзина пустая'):
            app.checkout.assert_the_cart_is_emply()
