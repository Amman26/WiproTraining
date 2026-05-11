import pytest


def get_element(my_list, index):
    return my_list[index]


def test_index_error():
    with pytest.raises(IndexError):
        get_element([1, 2, 3], 10)