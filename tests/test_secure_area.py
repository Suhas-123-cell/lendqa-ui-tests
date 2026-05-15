from playwright.sync_api import expect


def test_secure_area_heading_visible(logged_in):
    expect(logged_in.heading).to_be_visible()
    expect(logged_in.heading).to_contain_text("Secure Area")


def test_logout_button_is_visible(logged_in):
    expect(logged_in.logout_button).to_be_visible()


def test_logout_redirects_to_login(logged_in):
    logged_in.logout()
    expect(logged_in.page).to_have_url("https://the-internet.herokuapp.com/login")


def test_logout_shows_logged_out_message(logged_in):
    logged_in.logout()
    expect(logged_in.flash_message).to_contain_text("You logged out of the secure area")


def test_cannot_access_secure_area_without_login(login_page):
    # Try to go directly to the secure page without logging in
    login_page.page.goto("https://the-internet.herokuapp.com/secure")
    # Should be redirected back to login
    expect(login_page.page).to_have_url("https://the-internet.herokuapp.com/login")
