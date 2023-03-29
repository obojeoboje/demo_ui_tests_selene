import os

import allure
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser, config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=os.getenv("SELENOID_URL"),
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = 'https://staya.dog'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
