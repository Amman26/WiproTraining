from pages.home_page import HomePage


def test_invalid_login(driver):
    home = HomePage(driver)

    login_page = home.click_login()

    login_page.login("pavanol", "wrongpassword")

    alert_text = login_page.get_alert_text()

    # Intentional failure
    assert alert_text == "Success"

    return self.find(by_locator).text