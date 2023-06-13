class FormPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("input[name=\"username\"]")
        self.submit_button = page.get_by_role("button", name="submit")

    def navigate(self):
        self.page.goto("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    def fill(self):
        self.username_field.fill("Username")
        self.submit_button.click()