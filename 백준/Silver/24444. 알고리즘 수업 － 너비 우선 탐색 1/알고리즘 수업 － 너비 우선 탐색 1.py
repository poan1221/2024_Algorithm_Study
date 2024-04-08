# 정점의 수 n , 간선의 수 m, 시작 정점 r
# 양방향 간선...?

# 5 <= n <= 100,000 이므로 제한 늘려주기
import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(idx):
    global cnt

    q = deque([r])
    visited[r] = cnt  # 방문하면 순서 표시

    while q:
        idx = q.popleft()
        graph[idx].sort()  # 오름차순으로 진행해야 해서

        for i in graph[idx]:  # 인접 노드에서
            if visited[i] == 0:  # 접근하지 않은 것이면?
                cnt += 1
                visited[i] = cnt
                q.append(i)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 1부터 시작이니까.. n+1 까지, 방문 순서를 저장한다. 0이면 방문하지 않음
visited = [0] * (n + 1)
cnt = 1  # 방문 숫자니까 1부터 넣음

# 양방향 간선 그래프 넣어주기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 너비 우선 탐색
bfs(r)

# 방문한 결과를 출력
for i in range(1, n + 1):
    print(visited[i])
