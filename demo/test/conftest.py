import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def chrome(request):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def firefox(request):
    service = Service(executable_path=GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.binary_location = shutil.which("firefox")
    driver = webdriver.Firefox(service=service, options=options)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()