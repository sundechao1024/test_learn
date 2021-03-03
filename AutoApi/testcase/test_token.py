import requests

class TestGetToken:

    def test_get_token(self):


        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {'corpid' :'wwbadb96d36ea791c9',
                  'corpsecret' :'UjPx1NNR6E8kn70Xa-pY2SAGANTiYZSwIJCM-urt9Ok'
        }

        r = requests.get(url=url, params=params)
        print(r.json())