from selenium import webdriver
import time

class Test_login():

    def setup_method(self):
        self.wb = webdriver.Chrome()
        self.wb.implicitly_wait(7)

    def teardown_method(self):
        pass

    def test_login(self):
        self.wb.get('http://10.179.162.156:8990/pope-engine#/allactivity')
        self.wb.switch_to.frame(self.wb.find_element_by_xpath('/html/body/iframe[2]'))
        self.wb.find_element_by_id('username').send_keys('sundechao_v')
        self.wb.find_element_by_id('password').send_keys('Sdc971024@')
        self.wb.find_element_by_xpath('//*[@id="app"]/div/div[1]/main/button').click()
        time.sleep(5)
        self.wb.find_element_by_id('nv-plus').click()

