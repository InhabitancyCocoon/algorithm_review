from my_sort import Heap
from random import randint
import random


def test_min_heap() -> None:
    arr = list(randint(1, 15) for _ in range(17))
    heap = Heap(arr)
    assert heap.peak() == min(arr)
    heap.push(-1)
    assert heap.pop() == -1
    heap.push(-3)
    heap.push(-7)
    assert heap.pop() == -7
    assert heap.pop() == -3
    arr.sort(reverse=True)
    for _ in range(9):
        assert heap.pop() == arr.pop()
