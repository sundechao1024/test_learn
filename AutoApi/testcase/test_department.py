import requests
import json
class TestDepartment:
    def setup(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {'corpid': 'wwbadb96d36ea791c9',
                  'corpsecret': 'Wo4KTizdV2G30n7CM6LkjTE6hEiaefND270I9J9P8xc'
                  }

        r = requests.get(url=url, params=params)
        self.token = r.json()['access_token']
        print(self.token)

    def test_creat_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        param = {
            'access_token': self.token
        }
        data = {
               "name": "洪四闲",
               "name_en": "HSX",
               "parentid": 1,
               "order": 1234,
               "id": 2432
        }

        creatpost = requests.post(url=url, json=data, params=param)
        assert 'created'== creatpost.json()['errmsg']

    def test_updata_department(self):
         pass

    def test_delete_department(self):
        pass 
