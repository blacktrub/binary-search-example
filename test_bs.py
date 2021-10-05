from bs import EMPTY_VALUE
from bs import binary_search


def test_empty_binary_search():
    assert binary_search([], 1) == EMPTY_VALUE


def test_two_elements():
    assert binary_search([1, 2], 1) == 0


def test_first_middle_element():
    assert binary_search([1, 2, 3], 2) == 1


def test_last_element():
    assert binary_search([1, 2, 3], 3) == 2


def test_first_element():
    assert binary_search([1, 2, 3], 1) == 0


def test_second_element_in_big_array():
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 3) == 2
