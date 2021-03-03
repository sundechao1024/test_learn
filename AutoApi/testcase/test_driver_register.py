import AutoApi.api.driver_register
import pytest

class Test_driver_register:

    @pytest.mark.parametrize('test_phone',[('00017001428')])
    def test_driver_register_auto(self,test_phone):
        post_res = AutoApi.api.driver_register.driver_register().driver_register_auto(test_pohone=test_phone)
        assert post_res['msg'] == "Success"

    @pytest.mark.parametrize('test_phone',[('00017001427')])
    def test_driver_register(self,test_phone):
        post_res = AutoApi.api.driver_register.driver_register().driver_register_auto(test_pohone=test_phone)
        assert post_res['msg'] == "Success"
