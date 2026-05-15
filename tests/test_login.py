from playwright.sync_api import expect


def test_login_page_loads(login_page):
    login_page.goto()
    expect(login_page.page).to_have_title("The Internet")


def test_login_form_elements_visible(login_page):
    login_page.goto()
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


def test_valid_login_redirects_to_secure_area(login_page):
    login_page.goto()
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.page).to_have_url("https://the-internet.herokuapp.com/secure")


def test_valid_login_shows_success_message(login_page):
    login_page.goto()
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.success_message).to_be_visible()
    expect(login_page.success_message).to_contain_text("You logged into a secure area")


def test_wrong_password_shows_error(login_page):
    login_page.goto()
    login_page.login("tomsmith", "wrongpassword")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Your password is invalid")


def test_wrong_username_shows_error(login_page):
    login_page.goto()
    login_page.login("nobody", "SuperSecretPassword!")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Your username is invalid")


def test_empty_username_shows_error(login_page):
    login_page.goto()
    login_page.login("", "SuperSecretPassword!")
    expect(login_page.error_message).to_be_visible()


def test_empty_password_shows_error(login_page):
    login_page.goto()
    login_page.login("tomsmith", "")
    expect(login_page.error_message).to_be_visible()
