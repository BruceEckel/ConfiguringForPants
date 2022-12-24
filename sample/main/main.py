import sys
from colors import green
from util.string import concat


def message():
    return concat("Hello", "world!")


def print_message():
    print(green(message()))


if __name__ == "__main__":
    print_message()
    print(f"{sys.version = }")
