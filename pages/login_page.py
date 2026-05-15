class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator('button[type="submit"]')
        self.success_message = page.locator(".flash.success")
        self.error_message = page.locator(".flash.error")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
