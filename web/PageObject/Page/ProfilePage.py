from web.PageObject.Page.BasePage import BasePage


class ProfilePage(BasePage):

    def gotoSelected(self):
        return SelectPage()