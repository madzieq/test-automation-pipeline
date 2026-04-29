from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # URL of the test login page
    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        """ Initializes the LoginPage with a WebDriver instance. """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """ Opens the login page in the browser. """
        self.driver.get(self.URL)

    def enter_username(self, username):
        """ Enters the given username into the username field. """
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)

    def enter_password(self, password):
        """ Enters the given password into the password field. """
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)

    def click_login(self):
        """ Clicks the login button to submit the form. """
        self.wait.until(EC.element_to_be_clickable(self.BUTTON)).click()

    def get_flash_message(self):
        """ Returns the text of the flash message displayed after login attempt. """
        return self.wait.until(
            EC.visibility_of_element_located(self.FLASH_MESSAGE)
        ).text

    def login(self, username, password):
        """
        Performs a full login action: opens page, enters credentials and clicks login.
        Combines open(), enter_username(), enter_password() and click_login().
        """
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()