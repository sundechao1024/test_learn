import requests
import json


class Add_Driver():

    # 添加司机,传入司机手机号、车头ticket、测试账号的did
    def add_driver(self, testphone='',
                   partnert_icket='',
                   test_did=''):
        # 请求链接
        add_url = 'http://10.189.37.164:8000/api/v1/driver/sendBindInvite'
        # 请求参数
        add_params_strategy_info = [
            {"deduct_type": 1, "amount": "24",
             "switch": 'true',
             "effective_time": 0,
             "strategy_type": 0,
             "start_time": ""}]
        add_params = {"driver_phone": testphone,
                      "country_calling_code": "",
                      "driver_info": {},
                      "passport_info": {},
                      "strategy_info": json.dumps(
                          add_params_strategy_info),
                      "did": test_did,
                      "lang": "ru-RU",
                      'location_country': "RU",
                      "location_cityid": 7810200,
                      "locale": "ru_RU",
                      "utc_offset": 180,
                      "bundle_id": "com.didiglobal.fleet",
                      "from_fleetPC": 1,
                      "ticket": partnert_icket}
        # 发送请求
        add_post = requests.post(url=add_url,
                                 data=add_params)
        # 返回rs信息
        return add_post.json()
