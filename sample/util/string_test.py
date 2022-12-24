from util.string import concat

def test_string_concat() -> None:
    result = concat("hello", "world")
    assert result == "hello world"
