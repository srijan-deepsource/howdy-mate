import os
from contextlib import contextmanager

from pkg import howdy


@contextmanager
def override_howdy(greet_name):
    """Override the environment variable, and say Howdy."""
    old_name = os.environ.get('GREET_NAME')
    os.environ['GREET_NAME'] = greet_name
    yield
    os.environ['GREET_NAME'] = old_name or ''

def main():
    """Run the main function."""
    name = input("Who do you want to say Howdy to? ")
    with override_howdy(name):
        howdy.greet_me()

if __name__ == '__main__':
    main()
