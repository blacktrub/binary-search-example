from bs import EMPTY_VALUE
from bs import recursive_binary_search, loop_binary_search


def test_binary_search():
    for implementation in (recursive_binary_search, loop_binary_search):
        assert implementation([], 1) == EMPTY_VALUE
        assert implementation([1, 2], 1) == 0
        assert implementation([1, 2, 3], 2) == 1
        assert implementation([1, 2, 3], 3) == 2
        assert implementation([1, 2, 3], 1) == 0
        assert implementation([1, 2, 3, 4, 5, 6, 7], 3) == 2
