from typing import List

# find bridges and cut points in an undirected graph in liner time


def tarjan_bridge(edges: List[List[int]], n: int) -> List[int]:
    '''
    edges: List[List[int]], [a, b] represents an edge from a to b. The index starts from zero.
    n: number of vertices

    return: edges that are bridges which connect two subgraph.

    test: https://leetcode.cn/problems/critical-connections-in-a-network/description/
    '''

    idx = 2
    m = len(edges)
    e, bridge = [-1] * (2 * m + 7), [0] * (2 * m + 7)
    ne = [-1] * (2 * m + 7)
    he = [-1] * (n + 7)

    def add(a: int, b: int) -> None:
        nonlocal idx
        e[idx] = b
        ne[idx] = he[a]
        he[a] = idx
        idx += 1

    def dfs(a: int, in_edge: int) -> None:
        nonlocal ts
        dfn[a] = low[a] = ts
        ts += 1
        i = he[a]
        while i != -1:
            b = e[i]
            if not dfn[b]:
                dfs(b, i)
                low[a] = min(low[a], low[b])
                if low[b] > dfn[a]:
                    bridge[i] = bridge[i ^ 1] = 1
            elif i != in_edge ^ 1:
                low[a] = min(low[a], dfn[b])
            i = ne[i]

    for a, b in edges:
        add(a, b)
        add(b, a)

    dfn, low = [0] * n, [0] * n
    ts = 1

    for a in range(n):
        if not dfn[a]:
            dfs(a, 0)

    return [edges[i // 2] for i in range(0, 2 * m, 2) if bridge[i + 2]]
