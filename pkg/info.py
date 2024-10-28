# Store constants for the package
import os

GREET_NAME = os.environ.get('GREET_NAME', "Stranger")


def set_default_greet_name():
    """Return the name to greet."""
    if GREET_NAME:
        return GREET_NAME

    return "Stranger"

if __name__ == '__main__':
    set_default_greet_name()
