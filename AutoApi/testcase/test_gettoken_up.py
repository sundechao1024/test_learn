import pytest
import requests

class TestGetToken:

    @pytest.mark.parametrize('corpid,corpsecret,errmsg',
                             [('wwbadb96d36ea791c9','Wo4KTizdV2G30n7CM6LkjTE6hEiaefND270I9J9P8xc','ok')
                                 ,('','Wo4KTizdV2G30n7CM6LkjTE6hEiaefND270I9J9P8xc','corpid missing'),
                              ('wwbadb96d36ea791c9','','corpsecret missing')])
    def test_get_token(self,corpid,corpsecret,errmsg):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        r = requests.get(url=url)
        print(r.json())
        assert r.json()['errmsg'] == errmsg