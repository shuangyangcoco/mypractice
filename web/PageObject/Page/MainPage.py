from web.PageObject.Page.BasePage import BasePage
from web.PageObject.Page.SearchPage import SearchPage

class MainPage(BasePage):

    def search(self, keyword):
        self.driver.find_element_by_name("q").send_keys(keyword)
        self.driver.find_element_by_css_selector(".icon.iconfont").click()
        return SearchPage(self.driver)

    def profile(self):
        pass