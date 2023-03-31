import allure
from app import app


class TestCollections:
    @allure.parent_suite("Web")
    @allure.suite("Filters")
    @allure.title("Collections is visible")
    def test_collections(self):
        app.main.open_main_page()
        with allure.step('Перейти в каталог'):
            app.header_menu.choose_section("Каталог")
        with allure.step('Выбрать коллекцию'):
            app.catalog.choose_collection("Mono Yellow")
        with allure.step('Проверить что отображаются товары этой коллекции'):
            app.catalog.assert_collection("Mono Yellow")


class TestNewProducts:
    @allure.parent_suite("Web")
    @allure.suite("Filters")
    @allure.title("New products is visible")
    def test_new_products(self):
        app.main.open_main_page()
        with allure.step('Перейти в каталог'):
            app.header_menu.choose_section("Каталог")
        with allure.step('Выбрать новинки'):
            app.catalog.choose_new_products()
        with allure.step('Проверить, что отображаются новые товары'):
            app.catalog.assert_new_products()


class TestCharityProducts:
    @allure.parent_suite("Web")
    @allure.suite("Filters")
    @allure.title("Charity products is visible")
    def test_charity_products(self):
        app.main.open_main_page()
        with allure.step('Перейти в каталог'):
            app.header_menu.choose_section("Каталог")
        with allure.step('Выбрать Добро вместе'):
            app.catalog.choose_charity_products()
        with allure.step('Проверить, что отображаются товары с Добро вместе'):
            app.catalog.assert_charity_products()
