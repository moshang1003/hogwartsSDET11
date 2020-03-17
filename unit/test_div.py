# import json
import allure
import pytest

from unit.div import div


@pytest.mark.happy
def test_div_int():
    assert div(10, 2) == 5
    assert div(10, 5) == 2
    assert div(100000000, 1) == 100000000


# 参数化
@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,exception", {
    (10, 2, 5),
    (10, 5, 2),
    (100000000, 1, 100000000),
    (100, 200, 0.5)
})
def test_div_int_param(number1, number2, exception):
    assert div(number1, number2) == exception


# @pytest.mark.happy
# @pytest.mark.parametrize("number1,number2,exception",json.loads('1.json'))
# def test_div_int_add(number1,number2,exception):
# assert div(number1, number2) == exception
# 数组从外面的json导入


@pytest.mark.happy
# 分组标记
def test_div_float():
    assert div(10, 3) == 3.333333333333333
    assert div(10.2, 0.2) == 51


@pytest.mark.exception
def test_div_exception():
    assert div(10, 'a')
    assert div('abc', 10)


@pytest.mark.exception
# 分组标记
def test_div_zero():
    assert div(10, 0) == None


def test_div_fushu():
    assert div(-10, 2) == -5
    assert div(-10, -2) == 5


# 参数化
@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,exception", {
    (10, 2, 5),
    (10, 5, 2),
    (100000000, 1, 100000000),
    (100, 200, 0.5),
    (10, 3, 3.33),
    (10.2, 0.2, 51),
    (10, 'a', 'b'),
    ('abc', 10, 'd'),
    (10, 0, None),
    (0, 10, 0)
})
#可以用{}-set,集合，数据不可以重复,可也自动去重，也可以用[]-list或者()-元组表示数据列表
def test_div_int_param(number1, number2, exception):
    assert div(number1, number2) == exception


def test_a():
    assert 123 == 123
    allure.attach.file('C:/users/xlx/Desktop/123.png', attachment_type=allure.attachment_type.PNG)

def test_b():
    print(eval("1+2"))
    #EVAL:可直接执行eval后面括号里面的“string”代码提出来执行