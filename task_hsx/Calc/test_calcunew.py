#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 导入要使用的模块
import pytest
import pytest_ordering


# 定义测试计算机的类
class TestClacu1():

    # 定义测试加法的参数以及方法
    @pytest.mark.sum
    @pytest.mark.run(order=1)
    def testsum(self, get_addparam, get_calc):
        try:
            r = get_calc.add(get_addparam[0],
                             get_addparam[1])
        except TypeError:
            print("字符类型类型错误")
        else:
            if isinstance(r, float):
                r1 = round(r, 2)
                assert get_addparam[2] == r1
            else:
                assert get_addparam[2] == r

    # 定义测试除法的参数以及方法
    @pytest.mark.div
    @pytest.mark.run(order=4)
    def testdiv(self, get_divparam, get_calc):
        try:
            r = get_calc.div(get_divparam[0],
                             get_divparam[1])
        except ZeroDivisionError:
            print("被除数不能为0")
        except TypeError:
            print('输入有误，只能输入整数和小数')
        else:
            assert get_divparam[2] == r

    # 定义测试减法,并声名这个测试类为sub
    @pytest.mark.sub
    @pytest.mark.run(order=2)
    def testsub(self,get_calc,get_subparam):
        r = get_calc.sub(get_subparam[0],get_subparam[1])
        assert get_subparam[2] == r


    @pytest.mark.mul
    @pytest.mark.run(order=3)
    def checkmul(self,get_calc,get_mulparam):
        r = get_calc.mul(get_mulparam[0],get_mulparam[1])
        assert get_mulparam[2] == r