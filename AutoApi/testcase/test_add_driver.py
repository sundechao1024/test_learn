import pytest

import AutoApi.api.get_ticket
import AutoApi.api.add_driver

class Test_add_driver:


    # 添加司机,传入司机手机号和车头手机号
    @pytest.mark.parametrize('testphone,partnertphone',[('00017001427','00017001418'),('00017001419','00017001418'),('00017001427','00017001418'),('00017001428','00017001418')])
    def test_add_driver(self,testphone,partnertphone):
        # 获取车头ticket
        self.ticket = AutoApi.api.get_ticket.GetTicket().get_ticket(testphone=partnertphone)
        # 获取司机did
        self.did = AutoApi.api.get_ticket.GetTicket().get_did(testphone=testphone)
        # 调用添加司机的接口并传入参数
        add_driver_case = AutoApi.api.add_driver.Add_Driver().add_driver(testphone=testphone,test_did=self.did,partnert_icket=self.ticket)
        # 打印相关数据,或者断言
        assert  add_driver_case['errno'] == 0
        print(add_driver_case['errno'])
