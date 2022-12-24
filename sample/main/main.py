import sys
from colors import white
from util.string import concat


def message():
    return concat("Hello", "world!")


def print_message():
    print(white(message(), bg='green'))


if __name__ == "__main__":
    print_message()
    print(f"{sys.version = }")
