import pytest
from minimum_spanning_tree import kruskal, prim_n2, prim_mlgn
from typing import List, Callable


def test_mst_algorithm(func: Callable[[List[List[int]], int], int]) -> None:
    test_cases = [
        [
            [
                [0, 1, 2],
                [0, 3, 3],
                [0, 6, 4],
                [1, 2, 3],
                [1, 4, 2],
                [3, 4, 5],
                [4, 5, 7],
                [4, 6, 6],
            ],
            7,
        ],
        [[[0, 1, 2], [1, 2, 3], [0, 2, 4]], 3],
        [[[0, 1, 2], [1, 2, 3]], 3],
        [[[0, 0, 2]], 1],
    ]
    expected_outputs = [21, 5, 5, 0]
    for i, case in enumerate(test_cases):
        output = func(*case)
        assert (
            output == expected_outputs[i]
        ), f'case: {case}, expected: {expected_outputs[i]}, but got: {output}'


def test_kruskal() -> None:
    test_mst_algorithm(kruskal)


def test_prim() -> None:
    test_mst_algorithm(prim_mlgn)
    # test_mst_algorithm(prim_n2)
