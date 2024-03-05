from typing import List
import heapq


# edge: [from, to, weight], undirected simple graph, m: edges number, n: vertices number (index starts from 0)

inf = float("inf")


# O(mlgm)
def kruskal(edges: List[List[int]], n: int) -> int:
    edges.sort(key=lambda e: e[-1])

    fa = list(range(n))

    def find(x: int) -> int:
        if fa[x] == x:
            return x
        fax = find(fa[x])
        fa[x] = fax
        return fa[x]

    ans = 0

    for a, b, w in edges:
        if find(a) != find(b):
            fa[fa[a]] = b
            ans += w

    return ans


def prim_n2(edges: List[List[int]], n: int) -> int:
    adj = [[inf] * n for _ in range(n)]

    for a, b, w in edges:
        adj[a][b] = adj[b][a] = min(adj[a][b], w)

    d = [inf] * n
    d[0] = 0
    vis = [0] * n

    for _ in range(1, n):
        x = n + 7
        for j in range(n):
            if not vis[j] and (x == n + 7 or d[x] > d[j]):
                x = j
        vis[x] = 1
        for j in range(n):
            d[j] = min(d[j], adj[x][j])

    return sum(d)


def prim_mlgn(edges: List[List[int]], n: int) -> int:
    m = len(edges)
    e = [-1] * (m * 2 + 7)
    w = [-1] * (m * 2 + 7)
    he = [-1] * (n + 7)
    ne = [-1] * (m * 2 + 7)
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
        add(b, a, c)

    q = []
    vis = [0] * n
    d = [inf] * n

    i = he[0]
    vis[0] = True
    d[0] = 0

    while i != -1:
        q.append((w[i], e[i]))
        i = ne[i]

    heapq.heapify(q)

    while q:
        wi, ei = heapq.heappop(q)
        if vis[ei]:
            continue
        vis[ei] = 1
        d[ei] = wi
        i = he[ei]
        while i != -1:
            if not vis[e[i]]:
                heapq.heappush(q, (w[i], e[i]))
            i = ne[i]

    return sum(d)


if __name__ == "__main__":
    pass
