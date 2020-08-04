'''

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造

'''

from task_hsx.task_0731 import TongLao

class XuZhu(TongLao):

    def __init__(self):

        pass


    def reading(self):
        print("罪过罪过")

xz = XuZhu()
xz.reading()