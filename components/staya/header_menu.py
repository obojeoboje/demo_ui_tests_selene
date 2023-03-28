from selene import by, be
from selene.support.shared import browser

from locators.components import header_menu_locators


def press_log_in():
    browser.element(by.xpath(header_menu_locators.login_button)).click()

def check_log_in_button():
    browser.element(by.xpath(header_menu_locators.login_button)).should(be.visible)

def choose_section(section):
    browser.element(by.xpath(header_menu_locators.sections.format(text=section))).click()

def open_cart():
    browser.element(by.xpath(header_menu_locators.cart_button)).click()
