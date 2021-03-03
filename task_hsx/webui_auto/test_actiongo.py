from selenium import webdriver
from selenium.webdriver import ActionChains


class Test_Actionsgo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_move(self):
        self.driver.get('https://www.baidu.com/')
        setting_click = self.driver.find_element_by_id('s-usersetting-top')
        search_move = self.driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]')
        action = ActionChains(self.driver)
        action.click(setting_click)
        action.move_to_element(search_move)