import tempfile
import os
import pytest

import massox


def test_get_auth_from_env_variable_with_path():
    """
    GIVEN AuthManager
    WHEN the GOOGLE_APPLICATION_CREDENTIAL env variable is set with a valid path
    THEN the auth manager recognise it as a valid variable
    """

    tmp_file = tempfile.mkstemp()

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
        tempfile.gettempdir(), tempfile.gettempprefix()
    )

    from massox.authentication.authentication_manager import authentication_manager

    assert authentication_manager.is_compiled()
