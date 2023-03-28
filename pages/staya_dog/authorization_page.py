import allure
from selene.support.shared import browser
from selene import by
from locators.pages import authorization_locators


def type_email():
    browser.all(by.xpath(authorization_locators.input_email)).first.type("obojealexander@gmail.com")

def type_password():
    browser.all(by.xpath(authorization_locators.input_password)).first.type("Github505")

def submit_log_in():
    browser.element(by.xpath(authorization_locators.submit_button)).click()





