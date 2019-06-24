from web.PageObject.Page.BasePage import BasePage

class PostPage(BasePage):

    def publish(self, message, type='post'):
        button = {'post': '发布',
                  'apply_post': '支付并发布'}
        button_locator = '//*[@class="editor-container"]//*[text()={}]'.format(button[type])
        if message:
            self.driver.find_element_by_css_selector('.lite-editor__bd .medium-editor-element p').sendkey(message)
        self.driver.find_element_by_xpath(button_locator)


    def click_button(self, number):
        button_list = self.driver.find_element_by_css_selector('.lite-editor.lite-editor--tiny.editor--paste.expand.editor--storage .lite-editor__toolbar__btn')
        button_list[number].click()

    def addTopicByFace(self, face):
        face_mapping = {'笑': 0,
                        '大笑': 1,
                        '鼓鼓掌': 2,
                        '俏皮': 3,
                        '加油': 4,
                        '赚大了': 5,
                        '怒了': 6,
                        '哭泣': 7,
                        '亏大了': 8,
                        '困顿': 9,
                        '好失望': 10,
                        '滴汗': 11,
                        '为什么': 12,
                        '跪了': 13,
                        }

        #click button
        self.click_button(0)
        select_list = self.driver.find_element_by_css_selector(".lite-editor.lite-editor--tiny.editor--paste.expand.editor--storage .emoji__item img")
        self.publish(select_list[face_mapping[face]])

    def addTopicByStock(self, stock_name, stock_code):
        message = '${}({})$'.format(stock_name, stock_code)
        self.publish(message)

    def addTopicByAnswer(self, username):
        self.click_button(3)
        self.driver.find_element_by_css_selector('.lite-editor__bd .pay-mention__hd').sendkey(username)
        self.driver.find_element_by_xpath('//*[@class="pay-mention__item selected"]//*[contains(text(),"shuang_123")]').click()
        self.driver.find_element_by_xpath('//*[@class="modal modal__pay-mention"]//*[text()="确定"]').click()
        self.publish(type='apply_post')

    def addTopicByReward(self):
        self.click_button(4)
        self.driver.find_element_by_xpath('//*[@class="modal modal__pay-mention"]//*[text()="确定"]').click()
        self.publish(type='apply_post')

    def addTopicByLongContent(self):
        self.click_button(6)
        return LongContentPage(self.driver)

    def is_published(self, content , type="face"):
        type_mapping = {'face': 'img[@title="[{}]"]'.format(content),
                        'stock': 'a[text()="${}$"]'.format(content)}
        self.driver.find_element_by_xpath('//*[@class="timeline__item__main"]//*[contains(text(),"shuang_123")]/../../..//{}'.format(type_mapping[type]))
        return True






