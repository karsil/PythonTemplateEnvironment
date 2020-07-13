import pytest
import utils.demo as demo

def test_add_one():
    assert demo.add_one(1) == 2
    assert demo.add_one(-1) == 0

def test_sum_up_normal():
    my_sum = demo.sum_up([1, 2, 3])
    assert my_sum == 6

def test_sum_um_edgecases():
    assert demo.sum_up([]) == 0

def test_sum_up_exceptions():
    with pytest.raises(ValueError) as error_info:
        demo.sum_up(None)
    assert "Input must not be null!" in str(error_info)

def test_divide():
    assert demo.divide(4, 2) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e_info:
        demo.divide(4, 0)
    assert "Division by zero" in str(e_info)
