import requests
import json


class Get_actid():
    def get_actid(self,ticket=''):
        url = "http://10.156.32.83:8000/gulfstream/dive-honors/public/takeRate/run"
        data = {
            "ticket": ticket,
            "lang": "ru-RU",
            "city_id": "7999900",
            "canonical_country_code": "RU"}
        r = requests.post(url=url,params=data)
        return r.json()["data"]["activity_id"]

    def buy(self,actid='',ticket=''):
        url = 'http://10.156.32.83:8000/gulfstream/dive-honors/public/takeRate/buy'
        data = {
                "activity_id": actid,
                "ticket": ticket,
                "lang": "ru-RU",
                "utc_offset": "-180",
                "city_id": "7999900",
                "location_cityid": "7999900",
                "canonical_country_code": "RU"
            }
        r = requests.post(url=url,data = data)
        return r.json()


    #
    # # def buy(self):
    #     activity_id = Run().run()
    #     data = json.dumps({
    #         "activity_id": activity_id,
    #         "ticket": self.ticket,
    #         "lang": "ru-RU",
    #         "utc_offset": "-180",
    #         "city_id": "7999900",
    #         "location_cityid": "7999900",
    #         "canonical_country_code": "RU"
    #     })
    #     req = {
    #         "method": "post",
    #         "url": "http://10.156.32.83:8000/gulfstream/dive-honors/public/takeRate/buy",
    #         "data": data
    #     }
    #     r = self.send_requests(req)
    #     return r.json()
