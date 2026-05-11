import pytest


@pytest.fixture
def sample_dict():
    return {"name": "Alice", "role": "Dev"}


def test_dict_keys(sample_dict):
    # Check if "role" key exists
    assert "role" in sample_dict

    # Check value of "name"
    assert sample_dict["name"] == "Alice"