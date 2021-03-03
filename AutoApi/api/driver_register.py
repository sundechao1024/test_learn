import requests
import json

class driver_register:

    def driver_register_auto(self,test_pohone=''):
        url = 'http://10.190.0.174:7000/register/auto_register'
        params = {"env": "online", "product": 2,
                  "role": 1, "module": "register",
                  "isAutoVerify": 'false',
                  "phone": test_pohone,
                  "city": 7810200,
                  "country": "RU",
                  "fleetType": "ie"}
        res = requests.post(url=url,data=params)
        return res.json()

    def driver_register_auto(self,test_pohone=''):
        url = 'http://10.190.0.174:7000/register/auto_register'
        params = {"env":"online","product":2,"role":1,"module":"register","isAutoVerify":0,"phone":test_pohone,"city":7810200,"country":"RU"}
        res = requests.post(url=url,json=params)
        return res.json()