import yaml
from box import Box

from massox.authentication import authentication

config = None

# TODO: SET LOGGING


def set_config(path: str):
    try:
        with open(path) as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)

        config = Box(config)
    except FileNotFoundError as e:
        print(str(e))


if config is None:
    print(
        "Configs value is None - remember to set the value before using this package!"
    )
