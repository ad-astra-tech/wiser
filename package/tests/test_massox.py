import os
import pytest

import massox


def test_set_config():
    """
    GIVEN a valid path to a .yaml file
    WHEN set_config is called
    THEN massox' loads the config 
    """

    this_script_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(this_script_path, "stubs", "config", "config.yaml")

    assert massox.config == None

    massox.set_config(path=config_path)
