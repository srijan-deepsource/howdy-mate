"""Greet the world."""
from . import info


def greet_me():
    """Print a greeting."""
    print(f"Howdy, {info.GREET_NAME}!")


if __name__ == '__main__':
    greet_me()
