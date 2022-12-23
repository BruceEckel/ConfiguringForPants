from test_main.main import message

def test_message() -> None:
    assert message() == "Hi world"
