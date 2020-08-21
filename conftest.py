import pytest
import yaml
import os
import sys
from hogwartsgfis02.pythoncode.calc import \
    Calculator


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode(
            "utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode(
            "utf-8").decode("unicode_escape")


def get_root_dir():
    return os.path.dirname(os.path.dirname(
        os.path.dirname(__file__)))


sys.path.append(get_root_dir())

with open(r"E:\growth_autotest\learn\test_learn\/calcu.yml", encoding='UTF-8') as f:
    dates = yaml.safe_load(f)
    # 获取测试加法的参数
    add_param = dates['add']['add_params']
    # 获取加法测试用例的名称
    add_ids = dates['add']['add_ids']
    # 获取测试除法的参数
    div_param = dates["div"]['div_params']
    # 获取除法测试用例的名称
    div_ids = dates['div']['div_ids']
    # 获取测试减法的参数
    sub_param = dates["sub"]['sub_params']
    # 获取测试减法的用例名称
    sub_ids = dates["sub"]['sub_ids']
    # 获取测试乘法的参数
    mul_param = dates["mul"]['mul_params']
    # 获取测试乘法的用例名称
    mul_ids = dates["mul"]['mul_ids']

@pytest.fixture(scope='class')
def get_calc():
    clac = Calculator()
    print('打开计算器,开始执行测试用例')
    yield clac
    print('测试用例执行完毕')


@pytest.fixture(params=div_param, ids=div_ids)
def get_divparam(request):
    print('开始计算')
    yield request.param
    print('计算结束')


@pytest.fixture(params=add_param, ids=add_ids)
def get_addparam(request):
    print('开始计算')
    yield request.param
    print('计算结束')


@pytest.fixture(params=sub_param,ids=sub_ids)
def get_subparam(request):
    print('开始计算')
    yield request.param
    print('计算结束')

@pytest.fixture(params=mul_param,ids=mul_ids)
def get_mulparam(request):
    print('开始计算')
    yield request.param
    print('计算结束')