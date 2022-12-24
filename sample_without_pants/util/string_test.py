from util.string import concat

def test_string_concat() -> None:
    result = concat("hello", "world")
    assert result == "hello world"


if __name__ == '__main__':
    # Displays 'None' as a check to make sure it has run
    print(test_string_concat())
