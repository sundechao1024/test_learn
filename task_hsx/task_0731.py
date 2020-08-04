'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。


'''
# 定义一天上童姥的类,类名为TongLao
class TongLao():
    # 定位他的两个必传变量生命值和攻击力
    def __init__(self,TL_hp,TL_power):

        self.TL_hp = TL_hp
        self.TL_power = TL_power
    # 定位他的打招呼功能,看见人就喊话
    def see_popele(self,name):

        if name == 'WYZ':
            print("师弟！！！")
        elif name == '李秋水':
            print("呸，贱人")
        elif name == '丁春秋':
            print('叛徒！我杀了你')
        else:
            print(f'我不认识 {name}')

    # 定义他遇到敌人后进入攻击状态,将自己部分生命值转化为攻击力
    def fight_zms(self,foe_hp=0,foe_power=0):

        my_hp = (self.TL_hp / 2) - foe_power
        your_hp = foe_hp - (self.TL_power * 10)

        if my_hp > your_hp:
            print('天上童姥胜利,奥利给！')
        elif my_hp < your_hp:
            print('天上童姥失败,一Giao我里Giao')
        else:
            print('不要走！决战到天亮')
