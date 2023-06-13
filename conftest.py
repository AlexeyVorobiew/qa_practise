import allure
import requests
from requests.exceptions import HTTPError
import psycopg2
import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    BrowserType,
    Error,
    Page,
    Playwright,
    sync_playwright
)
from typing import  Generator

@pytest.fixture
def url():
    return "https://testpages.herokuapp.com/styled/basic-html-form-test.html"

@pytest.fixture
def chromium_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    return browser

@pytest.fixture
def chromium_page_context(chromium_browser,playwright: Playwright):

    context = chromium_browser.new_context()
    return context

@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page


##############################
###фикстуры для тестов БД
@pytest.fixture(scope="module")
def db_conn_params():
    return (DB_HOST, DB_NAME_DICT['INVENTORY'], DB_USER, DB_PASSWORD)

@pytest.fixture(scope="module")
def db_conn(db_conn_params):
    # Извлечение данных для подключения к БД Inventory из фикстуры db_inventory_conn_params
    host, dbname, user, password = db_conn_params

    # connect to DB
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=dbname
    )

    connection.set_client_encoding('UTF8')

    yield connection

    if connection:
        connection.close()

##############################
###класс для тестов АПИ (иллюстрация ООП)
class requestCore():
    def __init__(self, domain):
        self.domain = domain

    def GET(self, path, headers):
        try:
            url = f'{self.domain}{path}'
            print(url)
            with allure.step(f'GET request to: {url}'):
                return requests.get(url, headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

    def POST(self, path, data=None, json=None, headers=None):

        try:
            url = f'{self.domain}{path}'
            print(url)
            with allure.step(f'POST request to: {url}'):
                return requests.post(url=url, data=data, json=json, headers=headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')


##############################
###фикстуры для тестов АПИ
@pytest.fixture(scope="session")
def api_request():
    return requestCore(domain='https://api.thecatapi.com')