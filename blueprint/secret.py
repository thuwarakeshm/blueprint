import os


def print_secret():
    print(f"Let's keep it secret:{os.environ['APP_SECRET']}")
