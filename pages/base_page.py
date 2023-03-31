from selene.api import s, ss
from selene.support.conditions import be
from selene.support.shared import browser


class BasePage:

    def open_main_page(self):
        browser.open('')
