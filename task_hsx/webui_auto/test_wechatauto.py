from selenium import webdriver

from selenium.webdriver.common.by import By


# 定义一个类为wechat
class Test_wechat():
    # 设置前提步骤,1.启动浏览器 2.隐示等待上限5秒
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    # 设置结尾操作,关闭浏览器
    def teardown_method(self, method):
        self.driver.quit()

    # 定义上传文件的方法
    def test_uploadfilr(self):
        # 访问企业微信的首页
        self.driver.get(
            'https://work.weixin.qq.com/wework_admin/frame#inde')

        # 将cookie解析并添加到当前访问的网址中
        cookies = [
            {'domain': '.work.weixin.qq.com',
             'httpOnly': False,
             'name': 'wwrtx.vid', 'path': '/',
             'secure': False,
             'value': '1688851241085805'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': True,
             'name': 'wwrtx.vst', 'path': '/',
             'secure': False,
             'value': 'ItsyubSiLwa2bHCycnaV8VLhDhYQgm2GQ64Vv04HOmbthQ4osMS1P3C9Ao09ptjRoxPvgJOxm5YCJyi1ERImHlgOMl3MgTShvwO9Hey--mP13ZtmtbO3M64cGOdeMo_on1uNzFnUnNeXLRnldHpRvaxl5Qq3hZmFoSAxgDXXCTHzJuQuYvMpBckkjaQsZxd3ZpRPAmSgazAlCYMvvx5d0BAZvhrvjPBMgNGhbxmRvtK9L3iTW3JWyoB3KKZVdOQSbJS7QTkFwn6saPhVjTfrfg'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': False,
             'name': 'wxpay.vid', 'path': '/',
             'secure': False,
             'value': '1688851241085805'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': False,
             'name': 'wxpay.corpid', 'path': '/',
             'secure': False,
             'value': '1970324947154591'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': True,
             'name': 'wwrtx.sid', 'path': '/',
             'secure': False,
             'value': '1zfMdxxsdQab4zM4XzkYMn51aS_YS6kaw8XkYba4sAMGBvWYxdM2wzeVsqHa9q4i'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': False,
             'name': 'wwrtx.d2st', 'path': '/',
             'secure': False,
             'value': 'a2778117'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': True,
             'name': 'wwrtx.ltype', 'path': '/',
             'secure': False, 'value': '1'},
            {'domain': '.qq.com',
             'expiry': 2147385600,
             'httpOnly': False,
             'name': 'pgv_pvid', 'path': '/',
             'secure': False,
             'value': '1256357540'},
            {'domain': '.work.weixin.qq.com',
             'expiry': 1629527239,
             'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False,
             'value': '1597235602,1597978252,1597991066'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': True,
             'name': 'wwrtx.ref', 'path': '/',
             'secure': False, 'value': 'direct'},
            {'domain': 'work.weixin.qq.com',
             'expiry': 1598009778,
             'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False,
             'value': '6cr8rpl'},
            {'domain': '.qq.com',
             'expiry': 1598088267,
             'httpOnly': False, 'name': '_gid',
             'path': '/', 'secure': False,
             'value': 'GA1.2.1474626948.1597978254'},
            {'domain': '.work.weixin.qq.com',
             'httpOnly': True,
             'name': 'wwrtx.refid', 'path': '/',
             'secure': False,
             'value': '3413748341453214'},
            {'domain': '.qq.com',
             'expiry': 1912665776,
             'httpOnly': False, 'name': 'pac_uid',
             'path': '/', 'secure': False,
             'value': '0_640c65c77fcfc'},
            {'domain': '.work.weixin.qq.com',
             'expiry': 1600593869,
             'httpOnly': False,
             'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False,
             'value': 'zh-cn'},
            {'domain': '.qq.com',
             'expiry': 1661073867,
             'httpOnly': False, 'name': '_ga',
             'path': '/', 'secure': False,
             'value': 'GA1.2.1918874628.1597235604'},
            {'domain': '.work.weixin.qq.com',
             'expiry': 1628771597,
             'httpOnly': False,
             'name': 'wwrtx.c_gdpr', 'path': '/',
             'secure': False, 'value': '0'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 再次访问企业微信的首页或者刷新
        self.driver.get(
            'https://work.weixin.qq.com/wework_admin/frame#inde')

        # 通过css定位到上传的入口并点击
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.index_service_cnt_itemWrap:nth-child(2)').click()

        # 通过id定位到上传按钮上传文件
        self.driver.find_element_by_id(
            'js_upload_file_input').send_keys(
            r'E:\growth_autotest\learn\test_learn\testauto.xlsx')

        # 校验上传文件名是否符合预期
        assert 'testauto.xlsx' == self.driver.find_element_by_id(
            'upload_file_name').text
