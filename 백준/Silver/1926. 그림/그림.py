import sys
from collections import deque

input = sys.stdin.readline


# DFS 함수 정의
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1  # 방문 처리

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    area = 1  # 현재 노드 포함

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    area += 1
                    q.append((nx, ny))

    return area


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 그림의 개수와 가장 넓은 그림의 넓이를 찾기
cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            max_area = max(bfs(i, j), max_area)
            cnt += 1

print(cnt)
print(max_area)