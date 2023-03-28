import allure

from components.staya import header_menu
from pages.staya_dog import authorization_page, profile_page, main_page

@allure.parent_suite("Web")
@allure.suite("Authorization")
@allure.title("Log in to system")
def test_authorization(setup_browser):
    main_page.open_main_page()
    with allure.step('Press log in button'):
        header_menu.press_log_in()

    with allure.step('Type email'):
        authorization_page.type_email()

    with allure.step('Type password'):
        authorization_page.type_password()

    with allure.step('Press submit button'):
        authorization_page.submit_log_in()

    with allure.step('Check that orders page exists'):
        profile_page.check_orders_exists()


@allure.parent_suite("Web")
@allure.suite("Authorization")
@allure.title("Log out from system")
def test_logout(setup_browser):
    main_page.open_main_page()
    with allure.step('Open profile'):
        header_menu.open_profile()

    with allure.step('Log out from account'):
        profile_page.log_out()

    with allure.step('Submit logging out'):
        profile_page.log_out_submit()

    with allure.step('Check that log in button is available'):
        header_menu.check_log_in_button()

