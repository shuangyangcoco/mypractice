from time import sleep

import pytest
from selenium import webdriver


class TestSelenium(object):

    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://xueqiu.com/")
        cls.driver.implicitly_wait(10)

    def teardown_class(cls):
        sleep(10)
        cls.driver.quit()

    def test_install(self):
        driver = TestSelenium.driver
        driver.find_element_by_name("q").send_keys("alibaba")
        driver.find_element_by_css_selector(".icon.iconfont").click()
        driver.find_element_by_xpath("//*[contains(@href,'01688')]/../..//*[@class='iconfont']").click()
        driver.find_element_by_name("username").send_keys("xxxxxxsadf")
        driver.find_element_by_name("password").send_keys("asdfjsfasdf")
        driver.find_element_by_css_selector(".modal__login__btn").click()

