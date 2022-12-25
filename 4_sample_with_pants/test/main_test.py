from main.main import message

def test_message() -> None:
    assert message() == "Hello world!"

if __name__ == '__main__':
    # Displays 'None' as a check to make sure it has run
    print(test_message())
