import heapq
from typing import List
from collections import deque


# edge: [from, to, weight], directed simple graph, m: edges number, n: vertices number (index starts from 0)

inf = float('inf')


# O(mlgn)
def dijkstra(edges: List[List[int]], source: int, n: int) -> List[int]:
    e = [-1] * (2 * n + 7)
    w = [-1] * (2 * n + 7)
    he = [-1] * (n + 7)
    ne = [-1] * (2 * n + 7)
    idx = 1

    def add(a: int, b: int, c: int):
        nonlocal idx
        e[idx] = b
        w[idx] = c
        ne[idx] = he[a]
        he[a] = idx
        idx += 1

    for a, b, c in edges:
        add(a, b, c)

    q = []
    dist = [inf] * n
    dist[source] = 0
    q.append((0, source))
    vis = [False] * n

    while q:
        da, a = heapq.heappop(q)
        if vis[a]:
            continue
        vis[a] = True
        i = he[a]
        while i != -1:
            b = e[i]
            if dist[b] > da + w[i]:
                dist[b] = da + w[i]
                heapq.heappush(q, (dist[b], b))
            i = ne[i]

    return dist


# O(nm)
def bellman_ford(edges: List[List[int]], source: int, n: int) -> List[int]:
    dist = [inf] * n
    dist[source] = 0

    while True:
        change = False
        for a, b, c in edges:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                change = True
        if not change:
            break
    return dist


# O(km)
def bellman_ford_with_queue(edges: List[List[int]], source: int, n: int) -> List[int]:
    e = [-1] * (2 * n + 7)
    w = [-1] * (2 * n + 7)
    he = [-1] * (n + 7)
    ne = [-1] * (2 * n + 7)
    idx = 1

    def add(a: int, b: int, c: int):
        nonlocal idx
        e[idx] = b
        w[idx] = c
        ne[idx] = he[a]
        he[a] = idx
        idx += 1

    for a, b, c in edges:
        add(a, b, c)

    dist = [inf] * n
    dist[source] = 0
    q = deque()
    q.append(source)

    while q:
        s = len(q)
        vis = [0] * n
        for _ in range(s):
            a = q.popleft()
            i = he[a]
            while i != -1:
                b = e[i]
                if dist[b] > dist[a] + w[i] and not vis[b]:
                    q.append(b)
                    vis[b] = 1
                    dist[b] = dist[a] + w[i]
                i = ne[i]

    return dist


n = 3
edges = [[0, 1, 4]]
src = 0


if __name__ == '__main__':
    dist = dijkstra(edges, src, n)
    print(dist)
    dist = bellman_ford(edges, src, n)
    print(dist)
    dist = bellman_ford_with_queue(edges, src, n)
    print(dist)
