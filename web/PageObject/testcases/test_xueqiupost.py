from time import sleep

import pytest
import logging
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


from web.PageObject.Page.ProfilePage import ProfilePage
from web.PageObject.Page.MainPage import MainPage
from web.PageObject.testcases.BaseLog import BaseLog


class TestXueQiuSearch(BaseLog):

    def setup_class(cls):
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
        cls.driver.get("https://xueqiu.com/")
        cls.driver.implicitly_wait(10)
        cls.profile = ProfilePage(self.driver)
        self.profilepage.login()


    def teardown_class(cls):
        sleep(10)
        cls.driver.quit()

    def test_postbyface(self):
        self.profilepage.gotoPost().addTopicByFace('大笑')
        assert self.profilepage.gotoPost().is_published('大笑') == True

    def test_postbystock(self):
        self.profilepage.gotoPost().addTopicByStock('阿里巴巴(01688)')
        assert self.profilepage.gotoPost().is_published('阿里巴巴(01688)', 'stock') == True

    def test_postbyanswer(self):
        #can not test it for need to apply to monkey
        pass

    def test_postbyreward(self):
        #can not test it for need to apply to monkey
        pass

