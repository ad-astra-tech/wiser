import yaml
from box import Box

config = None


def set_config(path: str):
    try:
        with open(path) as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)

        config = Box(config)
    except FileNotFoundError as e:
        print(str(e))


if config is None:
    print(
        "Massox configs are None - remember to set the value before to use this package!"
    )
