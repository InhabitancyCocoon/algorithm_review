from typing import List
from collections import Counter, defaultdict


# arr = [random.randint(10, 99) for _ in range(100)]


def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        change = False
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                change = True
        if not change:
            break
    return arr


def merge_sort_imp(arr: List[int], l: int, r: int) -> None:
    if l >= r:
        return
    mid = l + r >> 1
    merge_sort_imp(arr, l, mid)
    merge_sort_imp(arr, mid + 1, r)
    tmp = arr[l : r + 1]
    i, j = l, mid + 1
    k = l
    while i <= mid and j <= r:
        if tmp[i - l] <= tmp[j - l]:
            arr[k] = tmp[i - l]
            i += 1
        else:
            arr[k] = tmp[j - l]
            j += 1
        k += 1
    while i <= mid:
        arr[k] = tmp[i - l]
        i += 1
        k += 1
    while j <= r:
        arr[k] = tmp[j - l]
        j += 1
        k += 1


def merge_sort(arr: List[int]) -> List[int]:
    merge_sort_imp(arr, 0, len(arr) - 1)
    return arr


def insert_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr


def chosen_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    left = 0
    while left < n - 1:
        ptr = left
        for i in range(left, n):
            if arr[i] < arr[ptr]:
                ptr = i
        arr[ptr], arr[left] = arr[left], arr[ptr]
        left += 1
    return arr


def heap_sort(arr: List[int]) -> List[int]:
    heap = Heap(arr)
    for i in range(len(arr)):
        arr[i] = heap.pop()
    return arr


def count_sort(arr: List[int]) -> List[int]:
    a, b = 10, 99
    cnt = Counter(arr)
    ptr = 0
    for i in range(a, b + 1):
        while cnt[i]:
            arr[ptr] = i
            cnt[i] -= 1
            ptr += 1
    return arr


def radix_sort(arr: List[int]) -> List[int]:
    bucket = defaultdict(list)
    digit = 3
    n = len(arr)

    for t in range(digit):
        for x in arr:
            d = x // (pow(10, t)) % 10
            bucket[d].append(x)
        i = 0
        for d in range(10):
            for x in bucket[d]:
                arr[i] = x
                i += 1
        bucket.clear()
    return arr


def quick_sort(arr: List[int]) -> List[int]:
    quick_sort_imp(arr, 0, len(arr) - 1)
    return arr


def quick_sort_imp(arr: List[int], l: int, r: int) -> None:
    if l >= r:
        return
    pivot = arr[r]
    ptr = l
    for i in range(l, r):
        if arr[i] < pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[r], arr[ptr] = arr[ptr], arr[r]
    quick_sort_imp(arr, l, ptr - 1)
    quick_sort_imp(arr, ptr + 1, r)


# Implement a min heap


class Heap:
    def __init__(self, arr: List[int] = []) -> None:
        self.n = len(arr)
        self.arr = list(arr)
        for i in range(self.n >> 1, -1, -1):
            self._sift_down(i)

    def _sift_down(self, i):
        min_idx = i
        l, r = i * 2 + 1, i * 2 + 2
        if l < self.n and self.arr[min_idx] > self.arr[l]:
            min_idx = l
        if r < self.n and self.arr[min_idx] > self.arr[r]:
            min_idx = r
        if min_idx != i:
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
            self._sift_down(min_idx)

    def pop(self):
        x = self.arr[0]
        self.arr[0], self.arr[self.n - 1] = self.arr[self.n - 1], self.arr[0]
        self.arr.pop()
        self.n -= 1
        self._sift_down(0)
        return x

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.n += 1
        self._sift_up(self.n - 1)

    def _sift_up(self, i: int):
        while i:
            fa = (i - 1) >> 1
            if self.arr[fa] > self.arr[i]:
                print(i, fa, self.arr[fa], self.arr[i])
                self.arr[fa], self.arr[i] = self.arr[i], self.arr[fa]
                i = fa
            else:
                break

    def peak(self) -> int:
        return self.arr[0]

    def __len__(self):
        return self.n
