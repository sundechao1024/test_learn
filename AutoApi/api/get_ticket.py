import requests

class GetTicket():

    # 通过手机号获取ticket
    def get_ticket(self,testphone=''):

        ticket_url = 'http://10.190.0.174:7000/register/driver_id'
        ticket_params = {"env":"online","product":2,"role":1,"module":"register","isAutoVerify":0,"country":"RU","city":'',"phone":testphone}

        # 发送请求并返回ticket
        r = requests.post(url=ticket_url,json=ticket_params)
        self.ticket = r.json()['data']['ticket']
        print(r.json()['data']['ticket'])
        return self.ticket

    # 通过手机号获取did
    def get_did(self,testphone=''):
        ticket_url = 'http://10.190.0.174:7000/register/driver_id'
        ticket_params = {"env":"online","product":2,"role":1,"module":"register","isAutoVerify":0,"country":"RU","city":'',"phone":testphone}

        # 发送请求并返回did
        r = requests.post(url=ticket_url,json=ticket_params)
        self.did = r.json()['data']['driver_id']
        print(r.json()['data']['driver_id'])
        return self.did

     # 通过手机号获取ticket-美东机房
    def get_ticket_us(self,testphone=''):

        ticket_url = 'http://10.190.0.174:7000/register/driver_id'
        ticket_params = {"env":"online","product":2,"role":1,"module":"register","isAutoVerify":0,"country":"RU_US","city":'',"phone":testphone}

        # 发送请求并返回ticket
        r = requests.post(url=ticket_url,json=ticket_params)
        self.ticket = r.json()['data']['ticket']
        print(r.json()['data']['ticket'])
        return self.ticket





