# 인접 토마토는 익는다
# 토마토 위치를 찾고 방향에 맞춰... 탐색 bfs
import sys
input = sys.stdin.readline

from collections import deque

def find_first(dq):
    for x in range(n):
        for y in range(m):
            if metrix[x][y] == 1:
                dq.append((x, y))

def find_way(x, y, d):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    return [x + dx[d], y + dy[d]]

def bfs():
    queue = deque()

    # 토마토 위치 찾기
    find_first(queue)

    # bfs 시작
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = find_way(x, y, d)

            if 0 <= nx < n and 0 <= ny < m and metrix[nx][ny] == 0:
                metrix[nx][ny] = metrix[x][y] + 1
                queue.append((nx, ny))


# input
m, n = map(int, input().split())
metrix = [list(map(int, input().split())) for _ in range(n)]

# bfs 로 메트릭스 갱신
bfs()

# 토마토 모두 익는 최초 날짜 출력 - 안 익은 거 있으면 -1
final_day = 0

for row in metrix:
    for tomato in row:
        if tomato == 0 :
            print(-1)
            exit()
        final_day = max(final_day, tomato)

print(final_day - 1)