import AutoApi.api.get_actid
import requests
import AutoApi.api.get_ticket

class Test_Buy():

    def test_buy(self):
        self.ticket = AutoApi.api.get_ticket.GetTicket().get_ticket_us('00017001267')
        self.act_id = AutoApi.api.get_actid.Get_actid().get_actid(ticket=self.ticket)
        buy_case = AutoApi.api.get_actid.Get_actid().buy(actid=self.act_id,ticket=self.ticket)
        print(buy_case)
        assert buy_case['errno'] == 0