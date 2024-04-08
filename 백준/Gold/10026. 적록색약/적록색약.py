# 적록색맹 - R 과 G 구분 못함
# 상하좌우 인접한 곳을 확인해서 두 개가 같으면 같은 구역으로

import sys
from collections import deque


# BFS 탐색해야하는 좌표
# 상하좌우
def bfs(x, y, red_check, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        # 총 4번의 위치 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 메트릭스 안에 있고, 이전 노드랑 인접 노드랑 값이 같고 이동하는 위치가 아직 안 간 곳이면
            if (
                0 <= nx < n
                and 0 <= ny < n
                and metrix[nx][ny] == metrix[x][y]
                and visited[nx][ny] == 0
            ):
                visited[nx][ny] = 1  # 방문 기록 체크
                q.append((nx, ny))


# 영역 카운트
def get_Area(red_check, visited):
    area = 0

    if not red_check:
        for i in range(n):
            for j in range(n):
                if metrix[i][j] == "G":
                    metrix[i][j] = "R"

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j, red_check, visited)
                area += 1

    return area


n = int(input())
# 그림판 받아오기
metrix = [list(map(str, input())) for _ in range(n)]

visited_nored = [[0] * n for _ in range(n)]
visited_red = [[0] * n for _ in range(n)]


print(get_Area(True, visited_red), get_Area(False, visited_nored))
