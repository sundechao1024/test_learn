from selenium import webdriver
from selenium.webdriver.chrome.options import \
    Options
from selenium.webdriver.common.by import By

from task_hsx.webui_auto.pages.add_member_page import \
    AddMemberPage
from task_hsx.webui_auto.pages.basepage import \
    BasePage
from task_hsx.webui_auto.pages.contact_page import \
    ContactPage

class MainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    _member = (By.CSS_SELECTOR,"[node-type='addmember']")
    _contact = (By.ID,'menu_contacts')
    def go_to_contact(self):
        self.find(*self._contact).click()
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.find(*self._member).click()
        return AddMemberPage(self.driver)