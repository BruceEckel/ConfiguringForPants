import sys
from colors import green
from util.string import string_concat


def message():
    return string_concat("Hi", " world")


def print_message():
    print(green(message()))


if __name__ == "__main__":
    print_message()
    print(f"{sys.version = }")
