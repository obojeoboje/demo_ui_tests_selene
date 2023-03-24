import allure
from selene.support.shared import browser
from pages.staya_dog import main_page, authorization_page, profile_page




@allure.parent_suite('Web')
@allure.suite('Авторизация')
@allure.title(f"Вход в систему")
def test_authorization(setup_browser):
    main_page.press_log_in()
    authorization_page.type_email()
    authorization_page.type_password()
    authorization_page.submit_log_in()
    profile_page.check_orders_exists()


@allure.parent_suite('Web')
@allure.suite('Авторизация')
@allure.title(f"Выход из системы")
def test_logout(setup_browser):
    profile_page.log_out()
    profile_page.log_out_submit()
    main_page.check_log_in_button()

