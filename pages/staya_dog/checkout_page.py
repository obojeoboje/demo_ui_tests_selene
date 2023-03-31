import allure
from selene.support.shared import browser
from selene import by, have, be, query
from locators.pages import checkout_locators
# from pages.staya_dog.product_page import ProductPage
from app import app
import random


class CheckoutPage:
    def assert_product_in_cart(self, collection_name, article_name):
        browser.element(by.xpath(checkout_locators.product_collection_name)).should(be.visible). \
            should(have.text(collection_name))
        browser.element(by.xpath(checkout_locators.product_article_name)).should(be.visible). \
            should(have.text(article_name))

    def clear_the_cart(self):
        browser.element(by.xpath(checkout_locators.clear_cart_button)).should(be.visible).click()

    def assert_the_cart_is_emply(self):
        browser.element(by.xpath(checkout_locators.empty_cart_message)).should(be.visible). \
            should(have.text("Товары отсутствуют"))
