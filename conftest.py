"""Fixtures: CLI options, the WebDriver (local Chrome or Selenoid/Remote),
page objects, and UI-based preconditions."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.urls import BASE_URL
from data.users import generate_user
from data.recipes import generate_recipe
from page_objects.main_page import MainPage
from page_objects.signup_page import SignUpPage
from page_objects.signin_page import SignInPage
from page_objects.recipe_create_page import RecipeCreatePage
from page_objects.recipe_page import RecipePage


def pytest_addoption(parser):
    parser.addoption("--selenoid-uri", action="store", default=None,
                     help="Selenoid hub URL; if set, runs via webdriver.Remote")
    parser.addoption("--browser-version", action="store", default="128.0",
                     help="Browser version requested from Selenoid")
    parser.addoption("--base-url", action="store", default=BASE_URL,
                     help="Service base URL under test")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run a local browser in headless mode")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
def driver(request):
    selenoid_uri = request.config.getoption("--selenoid-uri")
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")

    if selenoid_uri:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion",
                               request.config.getoption("--browser-version"))
        options.set_capability("selenoid:options",
                               {"enableVNC": True, "enableVideo": False})
        web_driver = webdriver.Remote(command_executor=selenoid_uri, options=options)
    else:
        web_driver = webdriver.Chrome(options=options)

    yield web_driver
    web_driver.quit()


@pytest.fixture
def new_user():
    return generate_user()


@pytest.fixture
def new_recipe():
    return generate_recipe()


@pytest.fixture
def main_page(driver, base_url):
    return MainPage(driver, base_url)


@pytest.fixture
def signup_page(driver, base_url):
    return SignUpPage(driver, base_url)


@pytest.fixture
def signin_page(driver, base_url):
    return SignInPage(driver, base_url)


@pytest.fixture
def recipe_create_page(driver, base_url):
    return RecipeCreatePage(driver, base_url)


@pytest.fixture
def recipe_page(driver, base_url):
    return RecipePage(driver, base_url)


@pytest.fixture
def registered_user(signup_page, new_user):
    """Precondition: a user registered through the UI. Returns its credentials."""
    signup_page.open_signup()
    signup_page.register(new_user)
    return new_user


@pytest.fixture
def authorized_user(registered_user, signin_page, main_page):
    """Precondition: a registered user logged in through the UI (by username)."""
    signin_page.open_signin()
    signin_page.login(registered_user["username"], registered_user["password"])
    main_page.is_logout_displayed()
    return registered_user
