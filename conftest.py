import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--br", action="store", default="chrome", help="the name of the browser")


@pytest.fixture
def driver():
    opts = ChromeOptions()
    opts.headless = True
    opts.add_argument("--window-size=1920,1080")
    opts.add_experimental_option("detach", True)
    opts.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
