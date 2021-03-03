from selenium import webdriver
from selenium.webdriver.chrome.options import \
    Options
from selenium.webdriver.common.by import By

from task_hsx.webui_auto.pages.basepage import \
    BasePage
from task_hsx.webui_auto.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID,'username')
    _memberAdd_acctid = (By.ID,'memberAdd_acctid')
    _memberAdd_phone = (By.ID,'memberAdd_phone')
    _save_member = (By.CSS_SELECTOR,'.js_btn_save')
    _cancel_member = (By.CSS_SELECTOR,'.js_btn_cancel')
    _confirm_cancel = (By.CSS_SELECTOR,'[node-type="cancel"]')

    def add_member(self,name, acctid, memberAdd_phone):
        self.find(*self._username).send_keys(name)
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        self.find(*self._memberAdd_phone).send_keys(memberAdd_phone)
        return self

    def save_member(self):
        self.find(*self._save_member).click()
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find(*self._cancel_member).click()
        self.find(*self._confirm_cancel).click()
        return ContactPage(self.driver)
