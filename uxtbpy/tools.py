import os
from contextlib import contextmanager


@contextmanager
def change_directory(destination: str):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
