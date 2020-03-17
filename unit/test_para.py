from logging import exception

import pytest

from unit.div import div


# 整数运算
@pytest.mark.parametrize("num1,num2,expect", {
    (10, 2, 5),
    (10, 5, 2),
    (100000000, 1, 100000000),
    (-10, 2, -5),
    (-10, -2, 5)
})
def test_para_int_param(num1, num2, expect):
    assert div(num1, num2) == expect


# 浮点数运算
@pytest.mark.parametrize("num1,num2,expect", {
    (10, 3, 3.3),
    (10.2, 0.2, 51),
    (-10, 2.1, -4.76)
})
def test_para_float_param(num1, num2, expect):
    assert div(num1, num2) == expect


# 为0计算
@pytest.mark.parametrize("num1,num2,expect", {
    (0, 3, 0),
    (0, -1, 0),
    (0,0,'none'),
    (1,0,'none')
})
def test_para_zero1_param(num1, num2, expect):
    assert div(num1, num2) == expect

# 非数字计算
@pytest.mark.parametrize("num1,num2,expect", {
    (10, 'a', 'Error'),
    ('a', 'b', 'Error')
})
def test_para_str_param(num1, num2, expect):
    assert div(num1, num2) == expect
