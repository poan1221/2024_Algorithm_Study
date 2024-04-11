import sys
from collections import deque

input = sys.stdin.readline


# 방향에 맞는 다음 위치 찾기
def find_way(x, y, d):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    return [x + dx[d], y + dy[d]]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    metrics[x][y] = 0  # 방문처리

    size = 1  # 현재 음식물 사이즈
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = find_way(x, y, d)

            # 다음 위치가 판 안에 있고, 음식물이 있는 1 일 때
            if 0 <= nx < N and 0 <= ny < M and metrics[nx][ny] == 1:
                metrics[nx][ny] = 0
                queue.append((nx, ny))
                size += 1
    return size


# 입력 데이터
N, M, K = map(int, input().split())

metrics = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    # 음식물 위치 표시
    metrics[r - 1][c - 1] = 1

# 최대 크기 찾기
max_size = 0
for i in range(N):
    for j in range(M):
        if metrics[i][j] == 1:
            max_size = max(max_size, bfs(i, j))


print(max_size)
