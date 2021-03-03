from selenium import webdriver

from task_hsx.webui_auto.pages.main_page import \
    MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()
        self.main.driver.implicitly_wait(5)

    def test_add_member(self):
        # 1.首页进入添加成员页面 2.添加成员
        namelist1 = self.main.go_to_add_member().add_member('sdc','sdc0','13187789769').save_member().get_membername()
        assert 'sdc' in namelist1

    def test_add_member_fail(self):
        # 1.首页进入添加成员页面 2.添加成员-失败案例
        namelist2 = self.main.go_to_add_member().add_member('fail','sdc0','13187789769').cancel_member().get_membername()
        assert 'fail' not in namelist2

    def test_contact_member(self):
        #1.首页进入通讯录 2.通讯录点击添加成员 3.添加成员
        namelist = self.main.go_to_contact().contact_add_member().add_member('alg1','al1g','11161178623').save_member().get_membername()
        assert 'alg1' in namelist


    def test_demo(self):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com/')