import yaml
# 定义方法game_1
def game_1():

    # 声名4个变量分别为我方血量、攻击力和敌方血量、攻击力
    date = yaml.safe_load(open('game.yaml'))
    print(date)
    my_hp = date['my']['hp']
    my_power = date['my']['power']
    littlebabyshit_hp = date['your']['hp']
    littlebabyshit_power = date['your']['power']
    # 循环打击,直至一方血量为0
    while True:
        # 血量计算方法,每一一次攻击血量都会减少,减少的血量等于对方的攻击力
        my_hp = my_hp - littlebabyshit_power
        littlebabyshit_hp = littlebabyshit_hp - my_power
        # 当我有一方血量为0,游戏技术停止游戏
        if my_hp <= 0:
            print("游戏结束,小屁孩获胜")
            break
        elif littlebabyshit_hp <= 0:
            print("游戏结束,洪四闲获胜")
            break
# 调用方法game_1
game_1()