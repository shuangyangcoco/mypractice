from time import sleep

import pytest
import logging
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


from web.PageObject.Page.MainPage import MainPage
from web.PageObject.testcases.BaseLog import BaseLog


class TestXueQiuSearch(BaseLog):

    def setup_class(cls):
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
        cls.driver.get("https://xueqiu.com/")
        cls.driver.implicitly_wait(10)
        cls.mainpage = MainPage(cls.driver)


    def teardown_class(cls):
        sleep(10)
        cls.driver.quit()

    def test_search(self):
        self.mainpage = TestXueQiuSearch.mainpage
        self.mainpage.search("alibaba").add_follow("01688")

    def test_profile(self):
        print(self.driver.get_cookies())
        self.driver.add_cookie({'name': 'bid', 'value': '2dceebd6406cbbe54461c0dd8ef044b8_jx4snce2'})
        self.driver.add_cookie({'name': 'device_id', 'value': '05630765f50fdd2443b683f2cec8e535'})
        self.driver.add_cookie({'name': 'Hm_lpvt_1db88642e346389874251b5a1eded6e3', 'value': '1561043146'})
        self.driver.add_cookie({'name': 'Hm_lvt_1db88642e346389874251b5a1eded6e3', 'value': '1560575143,1561040937'})
        self.driver.add_cookie({'name': 's', 'value':'dg1oomrfs9'})
        self.driver.add_cookie({'name': 'u', 'value': '9902319917'})
        self.driver.add_cookie({'name': 'u.sig', 'value': 'bHtqc0_AuKwoeU8ZrugjAcgHwh0'})
        self.driver.add_cookie({'name': 'xq_a_token', 'value': '15d750e78356f1f7fb59a95be35edcd84fb1dae4'})
        self.driver.add_cookie({'name': 'xq_a_token.sig', 'value': 'TgoDH1Fj-DnapBv7aHswu10gPgU'})
        self.driver.add_cookie({'name': 'xq_is_login', 'value': '1'})
        self.driver.add_cookie({'name': 'xq_is_login.sig', 'value': 'J3LxgPVPUzbBg3Kee_PquUfih7Q'})
        self.driver.add_cookie({'name': 'xq_r_token', 'value': 'f2d8cb01da8dec16c3155e70c24703bb4edf4295'})
        self.driver.add_cookie({'name': 'xq_r_token.sig', 'value': 'NkE5l3TZ_lwj2TL5r8lDEjbMj48'})
        self.driver.add_cookie({'name': 'xqat', 'value': '15d750e78356f1f7fb59a95be35edcd84fb1dae4'})
        self.driver.add_cookie({'name': 'xqat.sig', 'value': 'TMy3LZFPVXc08N27Mqgenxh_EvM'})

        self.driver.refresh()
        self.driver.get('https://xueqiu.com/users/connectnew?redirect=/setting/user')

    def test_log(self):
        self.log.debug("this is test debug log")
        self.log.info('this is test info log')
