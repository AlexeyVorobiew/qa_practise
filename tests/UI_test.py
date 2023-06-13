import allure
from playwright.sync_api import Page, expect
import allure
from form_page import FormPage
import os
import inspect

@allure.description("""
Заходим на страницу с веб формой
С помощью css локаторов выбираем формы ввода и отправлем данные
Проверяем, что имя юзернейма именно то, которое мы вводили
""")
def test_css_selectors(page, url) -> None:
    page.goto(url)
    page.locator("input[name=\"username\"]").click(timeout=3000) #пример явного ожидания (playwright использует auto-wait что приближенно можно назвать неявным ожиданием)
    page.locator("input[name=\"username\"]").fill("css_test_username")
    page.locator("css = #HTMLFormElements > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(2)").click() #пример абсолютного пути css
    page.locator("css = #HTMLFormElements > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(2)").fill("password")
    page.screenshot(path=f"tests/screens/{os.path.basename(__file__)}{inspect.stack()[0][3]}screenshot.png",
                    full_page=True) #пример скриншота
    page.get_by_role("button", name="submit").click()
    expect(page.locator("li[id=\"_valueusername\"]")).to_have_text("css_test_username")
    page.get_by_role("link", name="Go back to the form").click()
@allure.description("""
Заходим на страницу с веб формой
С помощью xpath локаторов выбираем формы, чекбоксы, кнопки и отправлем данные
Проверяем, что имя юзернейма именно то, которое мы вводили
""")
def test_xpath_selectors(page, url) -> None:
    page.goto(url)
    page.locator("xpath = //*[@name=\"username\"]").click()
    page.locator("xpath = //*[@name=\"username\"]").fill("xpath_test_username")
    page.locator("xpath = /html/body/div/div[3]/form/table/tbody/tr[2]/td/input").click() #пример абсолютного пути xpath
    page.locator("xpath = /html/body/div/div[3]/form/table/tbody/tr[2]/td/input").fill("password")
    page.get_by_role("button", name="submit").click()
    expect(page.locator("li[id=\"_valueusername\"]")).to_have_text("xpath_test_username")
    page.get_by_role("link", name="Go back to the form").click()

####иллюстрация page object model


def test_page_object(page, url) -> None:
    form_page = FormPage(page)
    form_page.navigate()
    form_page.fill()

