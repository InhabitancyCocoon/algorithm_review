import pytest
from single_source_shortest_path import dijkstra_mlgn, dijkstra_n2, bellman_ford, bellman_ford_with_queue
from typing import List, Callable

inf = float('inf')


def test_single_source_shortest_path(
    func: Callable[[[List[List[int]]], int, int], List[int]]
) -> None:
    test_cases = [
        [
            [
                [0, 1, 10],
                [0, 2, 3],
                [1, 3, 2],
                [2, 1, 4],
                [2, 3, 8],
                [2, 4, 2],
                [3, 4, 5],
            ],
            0,
            5,
        ],
        [[[0, 1, 5]], 0, 2],
        [[[0, 1, 3], [1, 2, 1], [2, 0, 4]], 0, 3],
        [[[0, 1, 5], [0, 2, 7], [1, 2, 2], [1, 3, 6], [2, 3, 4]], 1, 4],
        [[[0, 1, 3], [1, 2, 8], [2, 3, 4], [3, 0, 2]], 0, 4],
        [
            [
                [0, 1, 5],
                [1, 2, 4],
                [2, 3, 7],
                [3, 4, 6],
                [0, 4, 5],
                [2, 4, 3],
                [1, 4, 2],
            ],
            0,
            5,
        ],
        [[[0, 1, 4]], 0, 3],
        [[[0, 1, 5], [1, 2, 4], [2, 3, 3], [3, 4, 2], [0, 4, 6]], 0, 5],
        [
            [
                [0, 1, 6],
                [0, 3, 7],
                [1, 3, 8],
                [1, 2, 9],
                [1, 4, 5],
                [2, 4, 3],
                [3, 5, 4],
                [3, 4, 2],
                [4, 5, 1],
            ],
            0,
            6,
        ],
        [
            [
                [0, 1, 10],
                [0, 2, 3],
                [1, 3, 2],
                [2, 1, 4],
                [2, 3, 8],
                [2, 4, 2],
                [3, 4, 5],
            ],
            4,
            5,
        ],
    ]
    expected_outputs = [
        [0, 7, 3, 9, 5],
        [0, 5],
        [0, 3, 4],
        [inf, 0, 2, 6],
        [0, 3, 11, 15],
        [0, 5, 9, 16, 5],
        [0, 4, inf],
        [0, 5, 9, 12, 6],
        [0, 6, 15, 7, 9, 10],
        [inf, inf, inf, inf, 0],
    ]

    for i, test_case in enumerate(test_cases):
        output = func(*test_case)
        assert (
            output == expected_outputs[i]
        ), f'test case: {test_case}, expected: {expected_outputs[i]}, but got {output}'


def test_dijkstra() -> None:
    test_single_source_shortest_path(dijkstra_mlgn)
    test_single_source_shortest_path(dijkstra_n2)


def test_bellman_ford() -> None:
    test_single_source_shortest_path(bellman_ford)
    test_single_source_shortest_path(bellman_ford_with_queue)
