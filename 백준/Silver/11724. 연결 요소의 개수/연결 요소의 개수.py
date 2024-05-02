import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

# input
n , m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

connection = 0

# 모든 노드에 대해 dfs 수행
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        connection += 1

print(connection)