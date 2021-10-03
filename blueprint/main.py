import toml
from dotenv import load_dotenv

from .secret import print_secret

APP_CONFIG = toml.load("pyproject.toml")["app"]

load_dotenv()


def app():
    """This is the main entrypoint to your application"""
    print(f"This is {APP_CONFIG['APP_NAME']}. Let's build some cool python apps!")
    print_secret()
