import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    drver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    drver.maximize_window()
    yield drver
    drver.quit()