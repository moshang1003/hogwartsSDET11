
import pytest
import allure

import yaml

from unit.div import div


@pytest.mark.welldone
#@allure.title("welldone int")
@pytest.mark.parametrize("first_para, second_para, expected", yaml.safe_load(open("data.yaml")))
def test_div_int(first_para, second_para, expected):
    assert div(first_para, second_para) == expected




@pytest.mark.goodjob
@allure.title("goodjob float")
@pytest.mark.parametrize("first_para, second_para, expected",yaml.safe_load(open("data.yaml")))
def test_div_float(first_para, second_para, expected):
    assert abs(div(first_para, second_para) - expected) <= 0.1
 

@pytest.mark.exception
@allure.title("expected exception")
@pytest.mark.parametrize("first_para, second_para, expected", yaml.safe_dump(open("data.yaml")))
def test_div_error(first_para, second_para, expected):
    with pytest.raises(Exception) as exc_info:
        div(first_para, second_para)
    assert exc_info.type == expected
