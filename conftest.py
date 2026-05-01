import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Sets up and tears down a Chrome WebDriver instance for each test function.
    Uses Selenium Manager (built into Selenium 4.6+) to automatically
    download the correct ChromeDriver version.
    Runs in headless mode when executed inside Docker container.
    Browser window is maximized before the test and quit after.
    """
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")          # required in Docker
    options.add_argument("--no-sandbox")        # required in Docker
    options.add_argument("--disable-dev-shm-usage")  # required in Docker

    # Selenium Manager handles ChromeDriver automatically
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()