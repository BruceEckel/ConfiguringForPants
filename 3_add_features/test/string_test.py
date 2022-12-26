from util.string import concat

def test_string_concat() -> None:
    result = concat("word1", "word2")
    assert result == "word1 word2"

if __name__ == '__main__':
    # Displays 'None' as a check to show it has run
    print(test_string_concat())
