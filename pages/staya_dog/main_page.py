import allure
from selene.support.shared import browser
from selene import by, be
from locators.pages import staya_main_locators


def press_log_in():
    with allure.step(f'Press log in button'):
        browser.element(by.xpath(staya_main_locators.login_button)).click()

def check_log_in_button():
    with allure.step(f'Check that log in button is available'):
        browser.element(by.xpath(staya_main_locators.login_button)).should(be.visible)