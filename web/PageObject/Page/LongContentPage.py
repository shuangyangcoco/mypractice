from web.PageObject.Page.BasePage import BasePage

class LongContentPage(BasePage):
    def publishLongContent(self, content):
        self.driver.find_element_by_xpath(
            '//*[@aria-describedby="placeholder-ahkte"]//*[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"').sendkey(
            content)
        self.driver.find_element_by_css_selector('.publish_publish_1K9 .publish_button-dark_Nep').click()