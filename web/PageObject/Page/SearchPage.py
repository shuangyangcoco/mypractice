from web.PageObject.Page.BasePage import BasePage


class SearchPage(BasePage):

    def add_follow(self, keyword):
        locator = "//*[contains(@href, {})]/../..//*[@class='iconfont']".format(keyword)
        self.driver.find_element_by_xpath(locator).click()