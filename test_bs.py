from bs import binary_search, EMPTY_VALUE


def test_empty_binary_search():
    assert binary_search([], 1) == EMPTY_VALUE
