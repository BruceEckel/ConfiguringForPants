from util.math_utils import math_sum

def test_math_sum() -> None:
    result = math_sum(1, 10)
    assert result == 11
