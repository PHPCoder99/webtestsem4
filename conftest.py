import pytest, yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    response = requests.post(data["website1"], data={"username": data["username"], "password": data["password"]})
    if response.status_code == 200:
        return response.json()["token"]


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions
        driver = webdriver.Firefox(service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions
        driver = webdriver.Chrome(service, options=options)
    yield driver
    driver.quit()
