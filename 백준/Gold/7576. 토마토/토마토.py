# 익은 토마도 인접하면 하루 뒤에 익게 됨 - 혼자 익는 건 없음 > 일단 익어있는 토마토부터 구해야 함
# 인접 - 왼쪽 오른쪽 앞 뒤 4방향
# 다 익는 지 얼마나 걸리는 지 최소 날짜 구하기 - BFS

from collections import deque

# 입력값
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# BFS 탐색 초기 위치 찾기
tomatoes = deque()
for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            tomatoes.append((x, y))

# BFS 탐색 시작!
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while tomatoes:
    x, y = tomatoes.popleft()
    for d in range(4):
        # 한 칸씩 인접한 곳을 방향으로 따져서 다음 방향에 대한 것을 확인
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            # 처음 시작된 곳부터 +1 씩 늘어남 = 익은 날짜를 세는 것과 같음
            board[nx][ny] = board[x][y] + 1
            # 기준 토마토 위치 갱신
            tomatoes.append((nx, ny))

# 답 출력을 위한 함수
def find_max_day(board):
    max_day = 0
    for row in board:
        for tomato in row:
            # 못 익은 토마토가 있다면?
            if tomato == 0:
                return -1
            max_day = max(max_day, tomato)
    # 0 부터 센 거라 -1 해주기
    return max_day - 1


print(find_max_day(board))
