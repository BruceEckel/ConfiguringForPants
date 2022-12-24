import sys
from colored import fg, bg, attr
from util.string import concat


def message():
    return concat("Hello", "world!")


def print_message():
    print(f"{fg('22')} {bg(223)} {message()} {attr(0)}")


if __name__ == "__main__":
    print_message()
    print(f"{sys.version = }")
