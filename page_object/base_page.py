from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, xpath_element):
        WebDriverWait(self.driver, 50).until(ec.visibility_of_element_located((By.XPATH, f"{xpath_element}")))

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
    def send_key(self, locator, name):
        self.find_element(locator).clear()
        return self.find_element(locator).send_keys(name)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLow);")