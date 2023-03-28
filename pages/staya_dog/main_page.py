import os
from selene.support.shared import browser

def open_main_page():
    browser.config.hold_browser_open = True
    browser.open('')
    browser.config.window_width = 1920
    browser.config.window_height = 1080