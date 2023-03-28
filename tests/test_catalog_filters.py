import allure

from components.staya import header_menu
from pages.staya_dog import main_page, catalog_page


@allure.parent_suite("Web")
@allure.suite("Filters")
@allure.title("Collections is visible")
def test_collections(setup_browser):
    main_page.open_main_page()
    with allure.step('Перейти в каталог'):
        header_menu.choose_section("Каталог")
    with allure.step('Выбрать коллекцию'):
        catalog_page.choose_collection("Mono Yellow")
    with allure.step('Проверить что отображаются товары этой коллекции'):
        catalog_page.assert_collection("Mono Yellow")

@allure.parent_suite("Web")
@allure.suite("Filters")
@allure.title("New products is visible")
def test_new_products(setup_browser):
    main_page.open_main_page()
    with allure.step('Перейти в каталог'):
        header_menu.choose_section("Каталог")
    with allure.step('Выбрать новинки'):
        catalog_page.choose_new_products()
    with allure.step('Проверить, что отображаются новые товары'):
        catalog_page.assert_new_products()

@allure.parent_suite("Web")
@allure.suite("Filters")
@allure.title("Charity products is visible")
def test_charity_products(setup_browser):
    main_page.open_main_page()
    with allure.step('Перейти в каталог'):
        header_menu.choose_section("Каталог")
    with allure.step('Выбрать Добро вместе'):
        catalog_page.choose_charity_products()
    with allure.step('Проверить, что отображаются товары с Добро вместе'):
        catalog_page.assert_charity_products()