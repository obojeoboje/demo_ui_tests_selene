import allure
from selene.support.shared import browser
from selene import by, have
from locators.pages import profile_locators


def check_orders_exists():
    browser.element(by.xpath(profile_locators.my_orders)).should(have.text("Мои заказы"))

def log_out():
    browser.element(by.xpath(profile_locators.logout_button)).click()

def log_out_submit():
    browser.element(by.xpath(profile_locators.logout_button_submit)).click()

