from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest


@pytest.fixture(scope='class')
def yt_music_page():
    my_service = Service(executable_path=ChromeDriverManager().install())
    driver = Chrome(service=my_service)
    driver.get('https://music.youtube.com/playlist?list=RDCLAK5uy_nAJDvLXRZVjXclL2N3IjoCceuaM5T7o6Q')
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def chrome(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()