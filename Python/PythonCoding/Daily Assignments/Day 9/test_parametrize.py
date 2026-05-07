import pytest


@pytest.mark.parametrize("number", [2, 10, 22])
def test_is_even(number):
    assert number % 2 == 0