import os

import allure
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser, config


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    browser.config.base_url = os.getenv("URL")
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    # browser.open('')
    yield
    browser.quit()
