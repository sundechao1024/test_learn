from AutoApi.api.wework import Wework


class department(Wework):
    def setup(self):
        self.token = Wework.get_token()

    def creat_department(self):
        
        pass