from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def display_wait(self, drvier, local, value, message, times=10, interval=0.5, exception=None):
        WebDriverWait(drvier, times, interval, exception).until(
            EC.presence_of_element_located((local, value)), message=message)