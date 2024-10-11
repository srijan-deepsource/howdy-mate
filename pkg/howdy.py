"""Greet the world."""
from . import consts as constant


def greet_me():
    """Print a greeting."""
    print(f"Howdy, {constant.GREET_NAME}!")


if __name__ == '__main__':
    greet_me()
