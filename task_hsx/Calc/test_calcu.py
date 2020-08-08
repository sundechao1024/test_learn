#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 导入要使用的模块
import sys
import os
# sys.path.append('../..')
# from tools1.os_demo import get_root_dir
def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(get_root_dir())
from hogwartsgfis02.pythoncode.calc import Calculator
import pytest
import yaml


# 打开存储测试数据的文件并提取数据
with open("./calcu.yml", encoding='UTF-8') as f:
    dates = yaml.safe_load(f)
    # 获取测试加法的参数
    add_param = dates['add']['add_params']
    # 获取加法测试用例的名称
    add_ids = dates['add']['add_ids']
    # 获取测试除法的参数
    div_param = dates["div"]['div_params']
    # 获取除法测试用例的命中
    div_ids = dates['div']['div_ids']

# 定义测试计算机的类
class TestClacu():

    # 测试类执行前的动作
    def setup_class(self):
        self.calcu = Calculator()
        print("测试开始")

    # 测试类执行后的动作
    def teardown_class(self):
        print("测试结束")

    # 每次执行测试用例前的动作
    def setup(self):
        print('执行测试用例')

    # 每次执行测试用例后的动作
    def teardown(self):
        print('执行测试用例结束')

    # 定义测试加法的参数以及方法
    @pytest.mark.parametrize('a,b,result',
                             add_param,
                             ids=add_ids)
    @pytest.mark.sum
    def testsum(self, a, b, result):
        # if isinstance(a, (
        # int, float)) and isinstance(b,
        #                             (int, float)):
        #     r = round(self.calcu.add(a, b), 2)
        #     assert result == r
        #
        # else:
        #     pass
        # 当传入值有误时做相应处理,无误时对数据正常操作且与预期结果做比较
        try:
            r = self.calcu.add(a,b)
        except TypeError:
            print("字符类型类型错误")
        else:
            if isinstance(r, float):
                r1 = round(r, 2)
                assert result == r1
            else:
                assert result == r

    # 定义测试除法的参数以及方法
    @pytest.mark.parametrize('a,b,result',div_param,ids=div_ids)
    @pytest.mark.div
    def testdiv(self, a, b, result):
        try:
            r = self.calcu.div(a, b)
        except ZeroDivisionError:
            print("被除数不能为0")
        except TypeError:
            print('输入有误，只能输入整数和小数')
        else:
            assert result == r