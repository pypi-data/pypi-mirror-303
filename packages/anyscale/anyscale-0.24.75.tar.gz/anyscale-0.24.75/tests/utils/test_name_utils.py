import os

from anyscale.utils.name_utils import get_full_name


def test_get_full_name():
    for env_var in ["ANYSCALE_USERNAME", "USERNAME", "USER"]:
        if os.getenv(env_var):
            os.environ.pop(env_var)

    # Test sourcing priority
    assert get_full_name() == "default"
    os.environ["USER"] = "John Doe"
    assert get_full_name() == "john_doe"
    os.environ["USERNAME"] = "Jane   Smith"
    assert get_full_name() == "jane_smith"
    os.environ["ANYSCALE_USERNAME"] = "Ryan"
    assert get_full_name() == "ryan"
