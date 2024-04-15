import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# dfs
def dfs(idx, result):
    visited_dfs[idx] = True
    result.append(idx)

    for i in sorted(edges[idx]):
        if not visited_dfs[i]:
            dfs(i, result)


# bfs
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    result = []

    while queue:
        idx = queue.popleft()
        result.append(idx)

        for i in sorted(edges[idx]):
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)
    return result


# 입력
n, m, v = map(int, input().split())
# 양방향 간선 넣기
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited_dfs = [False] * (n + 1)
dfs_result = []
dfs(v, dfs_result)
print(" ".join(map(str, dfs_result)))

visited_bfs = [False] * (n + 1)
print(" ".join(map(str, bfs(v))))
