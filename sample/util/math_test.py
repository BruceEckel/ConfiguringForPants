from util.math import sum

def test_math_sum() -> None:
    result = sum(1, 10)
    assert result == 11

if __name__ == '__main__':
    # Displays 'None' as a check to make sure it has run
    print(test_math_sum())
