from web.PageObject.Page.BasePage import BasePage


class SelectPage(BasePage):
    def addSelect(self, stock_name, stock_type):
        self.driver.find_element_by_css_selector('.optional .search__dropdown input').sendkey(stock_name)
        self.driver.find_element_by_xpath("//*[@class='search__dropdown__list']//*[contains(text(),{})]".format(stock_type)).click()
        return self

    def getCurrentPrice(self, stockname):
        self.display_wait(
            self.driver,
            By.XPATH,
            '//*[@class="optional__tb optional_stocks"]//*[contains(text(),"01688")]',
            "not find this elements").click()
        current_price = self.driver.find_element_by_xpath('//*[@class="optional__tb optional_stocks"]//*[contains(text(),"01688")]/../../../td[2]').text()
        return float(current_price)



    

