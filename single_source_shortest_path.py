import heapq
from typing import List
from collections import deque


# edge: [from, to, weight], directed simple graph, m: edges number, n: vertices number (index starts from 0)

inf = float("inf")


# O(mlgn)
def dijkstra_mlgn(edges: List[List[int]], source: int, n: int) -> List[int]:
    m = len(edges)
    e = [-1] * (m + 7)
    w = [-1] * (m + 7)
    he = [-1] * (n + 7)
    ne = [-1] * (m + 7)
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


def dijkstra_n2(edges: List[List[int]], source: int, n: int) -> List[int]:
    adj = [[inf] * n for _ in range(n)]

    def add(a: int, b: int, c: int) -> None:
        adj[a][b] = c

    for a, b, c in edges:
        add(a, b, c)

    dist = [inf] * n
    vis = [False] * n

    dist[source] = 0

    for _ in range(1, n):
        x = n + 7
        for j in range(n):
            if not vis[j] and (x == n + 7 or dist[x] > dist[j]):
                x = j
        vis[x] = True
        for j in range(n):
            dist[j] = min(dist[j], dist[x] + adj[x][j])

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
    m = len(edges)
    e = [-1] * (m + 7)
    w = [-1] * (m + 7)
    he = [-1] * (n + 7)
    ne = [-1] * (m + 7)
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
    vis = [0] * n
    vis[source] = 1
    q = deque()
    q.append(source)

    while q:
        a = q.popleft()
        vis[a] = 0
        i = he[a]
        while i != -1:
            b = e[i]
            if dist[b] > dist[a] + w[i]:
                dist[b] = dist[a] + w[i]
                if not vis[b]:
                    vis[b] = 1
                    q.append(b)
            i = ne[i]

    return dist


n = 7
edges = [
    [0, 1, 2],
    [0, 3, 3],
    [0, 6, 4],
    [1, 2, 3],
    [1, 4, 2],
    [3, 4, 5],
    [4, 5, 7],
    [4, 6, 6],
]
m = len(edges)
for a, b, c in edges[:m]:
    edges.append([b, a, c])
src = 0


if __name__ == "__main__":
    dist = dijkstra_mlgn(edges, src, n)
    print(dist)
    dist = bellman_ford(edges, src, n)
    print(dist)
    dist = bellman_ford_with_queue(edges, src, n)
    print(dist)
