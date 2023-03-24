import allure
from selene.support.shared import browser
from selene import by, have
from locators.pages import profile_locators


def check_orders_exists():
    with allure.step(f'Check that orders page exists'):
        browser.element(by.xpath(profile_locators.my_orders)).should(have.text("Мои заказы"))

def log_out():
    with allure.step(f'Log out from account'):
        browser.element(by.xpath(profile_locators.logout_button)).click()

def log_out_submit():
    with allure.step(f'Submit logging out'):
        browser.element(by.xpath(profile_locators.logout_button_submit)).click()

