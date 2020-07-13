import pytest
import utils.demo as demo

class TestDemo:
    def test_add_one(self):
        assert demo.add_one(1) == 2
        assert demo.add_one(-1) == 0

    def test_sum_up_normal(self):
        my_sum = demo.sum_up([1, 2, 3])
        assert my_sum == 6

    def test_sum_um_edgecases(self):
        assert demo.sum_up([]) == 0

    def test_sum_up_exceptions(self):
        with pytest.raises(ValueError) as error_info:
            demo.sum_up(None)
        assert "Input must not be null!" in str(error_info)

    def test_divide(self):
        assert demo.divide(16, 4) == 4
        assert demo.divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError) as e_info:
            demo.divide(4, 0)
        assert "Division by zero" in str(e_info)
