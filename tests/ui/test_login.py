import pytest
from pages.login_page import LoginPage


class TestLogin:

    # Not parametrized: this test verifies a single, well-defined happy path
    # valid user + correct password
    # a valid user should always be redirected to the secure area.
    def test_successful_login(self, driver):
        """
        Test that a valid user can log in successfully.
        Verifies that the flash message confirms successful login.
        """
        page = LoginPage(driver)
        page.login("tomsmith", "SuperSecretPassword!")
        assert "You logged into a secure area!" in page.get_flash_message()

    # Parametrized: different invalid credential combinations are tested
    # to verify that the correct error message appears for each failed login attempt.
    @pytest.mark.parametrize("username, password, expected_message", [
        ("wronguser", "wrongpassword", "Your username is invalid!"),
        ("tomsmith", "wrongpassword", "Your password is invalid!"),
        ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
        ("", "", "Your username is invalid!"),
    ])
    def test_failed_login(self, driver, username, password, expected_message):
        """
        Test that invalid credentials result in an appropriate error message.
        Verifies that the flash message matches the expected error for each case.
        """
        page = LoginPage(driver)
        page.login(username, password)
        assert expected_message in page.get_flash_message()

    # Not parametrized: we are verifying a single UI behaviour —
    # the login form should be visible when the page is opened.
    def test_login_form_is_visible(self, driver):
        """
        Test that the login form elements are visible on page load.
        Verifies that username field, password field and login button are displayed.
        """
        page = LoginPage(driver)
        page.open()
        assert driver.find_element(*LoginPage.USERNAME).is_displayed()
        assert driver.find_element(*LoginPage.PASSWORD).is_displayed()
        assert driver.find_element(*LoginPage.BUTTON).is_displayed()