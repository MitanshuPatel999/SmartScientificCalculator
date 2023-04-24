from project import *
import pytest
import math


def test_calc():
    assert add(4,5)==9
    assert sub(4,5)==-1
    assert mul(4,5)==20
    assert div(4,5)==0.8
    assert square(5)==25
    assert sqrt(4,5)==2
    assert cube(4)==64
    assert power(2,3)==8
    assert fact(5)==120
    assert ln(math.e)==1
    assert log10(100)==2
    assert mod(11,8)==3


def test_findnumbers():
    assert findnumbers(["a","b","1","c","2"])==[1.0,2.0]
    assert findnumbers(["a", "b", "1", "c", "d"]) == [1.0, 0]
    with pytest.raises(ValueError):
        findnumbers(["add","1","2","3"])
        findnumbers(["hello"])


def test_raises():
    with pytest.raises(TypeError):
        click()
        audio()
