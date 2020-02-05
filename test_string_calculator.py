import pytest
from string_calculator import StringCalculator
"""
Copyright: @2019
Author: Zweli Mthethwa
"""
calculator = StringCalculator()

def test_add():
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    assert calculator.add("0,1,3,2") == 6
    assert calculator.add("1,2,3") == 6
    assert calculator.add("//;\n1;2") == 3
    assert calculator.add("//[***]\n1***2***3") == 6
    assert calculator.add("//[*][%]\n1*2%3") == 6
    # testing exceptions
    with pytest.raises(Exception) as e:
        assert calculator.add("-20,\n,3,2")
    assert str(e.value) == "negatives not allowed "+"-20"

    with pytest.raises(Exception) as e:
        assert calculator.add("-10,\n,-33,10, -79")
    assert str(e.value) == "negatives not allowed "+"-10,-33,-79"

    # testing for numbers bigger than 1000
    assert calculator.add("2, 1001") == 2
    assert calculator.add("//[(-_-')][%]\n1(-_-')2%3") == 6
