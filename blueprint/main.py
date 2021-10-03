import toml

APP_CONFIG = toml.load("pyproject.toml")["app"]


def app():
    """This is the main entrypoint to your application"""
    print(f"This is {APP_CONFIG['APP_NAME']}. Let's build some cool python apps!")
