import time

from selenium.webdriver.common.by import By

from task_hsx.webui_auto.pages.basepage import \
    BasePage


class ContactPage(BasePage):
    _add_member = (By.CSS_SELECTOR,'.ww_operationBar .js_add_member')
    _namelist = (By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
    def contact_add_member(self):
        # 解决循环导入问题
        from task_hsx.webui_auto.pages.add_member_page import \
            AddMemberPage
        # time.sleep(3)
        self.find(*self._add_member).click()
        return AddMemberPage(self.driver)

    def get_membername(self):
        # time.sleep(3)
        namelist = self.finds(*self._namelist)
        return [name.text for name in  namelist]