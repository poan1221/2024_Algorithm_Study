# 테스트 케이스 n 번
# 체스판 한 변의 길이, 현재 위치, 이동화려는 위치
# 이동 좌표,,,

import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# BFS 탐색해야하는 좌표
# [위2,오1], [위1, 오2], [아래1, 오2], [아래2, 오1], [아래2, 왼1], [아래1, 왼2], [위1, 왼2], [위2, 왼1]]
def bfs():
    dx = [1, 2, -1, -2, -2, -1, 1, 2]
    dy = [2, 1, 2, 1, -1, -2, -2, -1]

    knight = deque()
    knight.append((start_x, start_y))
    while knight:
        x, y = knight.popleft()

        # 이동 위치가 목표 위치가 되면
        if x == target_x and y == target_y:
            return chess[x][y] - 1

        # 총 8번의 위치 확인
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            # 체스판 내에 있고, 이동하는 위치가 아직 안 간 곳이면
            if 0 <= nx < one_len and 0 <= ny < one_len and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                knight.append((nx, ny))


n = int(input())
for _ in range(n):
    one_len = int(input())  # 체스판 한변의 길이
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    # 체스판 그려주기
    chess = [[0] * one_len for _ in range(one_len)]

    # 처음 위치 넣어주기
    chess[start_x][start_y] = 1

    # 출력
    print(bfs())
