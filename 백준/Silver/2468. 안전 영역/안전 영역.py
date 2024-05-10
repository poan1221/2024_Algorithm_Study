# 문제: 2468 안전 영역
import sys
input = sys.stdin.readline

from collections import deque

def find_way(x, y, d):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    return [x + dx[d], y + dy[d]]

def bfs(i, j, h):
    queue = deque([(i, j)])
    visited[i][j] = True

    # bfs 시작
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = find_way(x, y, d)

            # 범위 안에 있고, 방문하지 않았고, 비가 오는 높이보다 지대가 높다면
            if 0 <= nx < n and 0 <= ny < n and water_board[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 안전 영역 찾기 _ 특정 물 높이를 기준으로 잠기지 않은 영역 탐색
def safe_area(h):
    count = 0
    for i in range(n):
        for j in range(n):
            if water_board[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                count += 1
    return count

# input
n = int(input())
water_board = [list(map(int, input().split())) for _ in range(n)]

# 제일 높은 지대의 높이가 몇인지 찾기
max_height = 0
for row in water_board:
    max_height = max(max_height, max(row))

# 높이가 0인 것 최대 높이까지 안전 영역 개수 구하기
# 비가 안 오는 경우 포함하기 위해 최대 높이를 포함
    max_safe_area = 0
for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    max_safe_area = max(max_safe_area, safe_area(h))
    
print(max_safe_area)
