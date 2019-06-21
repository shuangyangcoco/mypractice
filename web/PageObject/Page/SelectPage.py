from web.PageObject.Page.BasePage import BasePage


class SelectPage(BasePage):

    def addSelect(self, stock_name, stock_type):
        self.driver.find_element_by_css_selector('.optional .search__dropdown input').sendkey(stock_name)
        self.driver.find_element_by_xpath("//*[@class='search__dropdown__list']//*[contains(text(),{})]".format(stock_type)).click()
        return self

    def getCurrentPrice(self, stockname):

    

