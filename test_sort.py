import pytest
import random
from my_sort import (
    merge_sort,
    insert_sort,
    heap_sort,
    count_sort,
    radix_sort,
    quick_sort,
    chosen_sort,
)
from typing import Callable, List


def test_sort_algorithm(func: Callable[[List[int]], None]):
    for _ in range(10):
        test_single_sample(func)


def test_merge_sort():
    test_sort_algorithm(merge_sort)


def test_insert_sort():
    test_sort_algorithm(insert_sort)


def test_heap_sort():
    test_sort_algorithm(heap_sort)


def test_count_sort():
    test_sort_algorithm(count_sort)


def test_radix_sort():
    test_sort_algorithm(radix_sort)


def test_quick_sort():
    test_sort_algorithm(quick_sort)


def test_chosen_sort():
    test_sort_algorithm(chosen_sort)


def test_single_sample(func: Callable[[List[int]], List[int]]):
    arr = [random.randint(10, 99) for _ in range(100)]
    expected_arr = sorted(arr)
    sorted_arr = func(arr)
    assert sorted_arr == expected_arr, f'Expect array: {expected_arr}, but got {arr}'
