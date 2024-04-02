import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
move = [[1, 0], [1, 1], [0, 1], [-1, 1]]
N = 19
win = 0

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:  # 돌이 있는 칸이면
            stone = board[i][j]  # 돌의 색 저장
            for dx, dy in move:
                cnt = 1  # 첫 돌 세주기
                nx, ny = i + dx, j + dy
                while (
                    0 <= nx < N and 0 <= ny < N and board[nx][ny] == stone
                ):  # 범위내에 있고, 해당 방향에 돌 색이 있다면
                    cnt += 1  # 범위내에 있고, 기존 돌 == 이동한 곳의 돌
                    # 오목이 됐으나 육목 체크
                    if cnt == 5:
                        if (
                            0 <= i - dx < N
                            and 0 <= j - dy < N
                            and board[i - dx][j - dy] == stone
                        ):  # 반대칸에 하나 더 있거나
                            break
                        if (
                            0 <= nx + dx < N
                            and 0 <= ny + dy < N
                            and board[nx + dx][ny + dy] == stone
                        ):  # 앞에 한칸에 더 있으면
                            break
                        else:
                            win = stone
                        x, y = i, j
                    # 이동 좌표
                    nx += dx
                    ny += dy
if win > 0:
    print(win)
    print(x + 1, y + 1)
else:
    print(0)
