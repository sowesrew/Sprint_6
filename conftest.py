import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.fullscreen_window()
    yield firefox_driver
    firefox_driver.quit()
