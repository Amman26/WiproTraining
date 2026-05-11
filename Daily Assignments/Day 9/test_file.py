import pytest
import os


@pytest.fixture
def temp_file():
    # Setup phase
    filename = "test.txt"

    with open(filename, "w") as file:
        file.write("Hello World")

    # Provide filename to the test
    yield filename

    # Teardown phase
    os.remove(filename)


def test_file_content(temp_file):
    with open(temp_file, "r") as file:
        content = file.read()

    assert content == "Hello World"