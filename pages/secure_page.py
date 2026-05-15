class SecurePage:
    def __init__(self, page):
        self.page = page
        self.heading = page.locator("h2")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.flash_message = page.locator(".flash")

    def logout(self):
        self.logout_button.click()
