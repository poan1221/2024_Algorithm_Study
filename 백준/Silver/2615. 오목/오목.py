import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
move= [[1,0],[1,1],[0,1],[-1,1]]
N = 19
win = 0

for i in range(N):
    for j in range(N):
        if board[i][j] != 0: # 돌이 있는 칸이면
            stone = board[i][j] # 돌의 색 저장
            for dy, dx in move:
                cnt = 1  # 첫 돌 세주기
                ny, nx = i + dy, j + dx
                while 0 <= ny < N and 0 <= nx < N and board[ny][nx] == stone: # 범위내에 있고, 해당 방향에 돌 색이 있다면
                    cnt += 1  # 범위내에 있고, 기존 돌 == 이동한 곳의 돌
                    # 오목이 됐으나 육목 체크
                    if cnt == 5:
                        if 0 <= i - dy < N and 0 <= j - dx < N and board[i-dy][j-dx] == stone: # 반대칸에 하나 더 있거나
                            break
                        if 0 <= ny + dy < N and 0 <= nx + dx < N and board[ny+dy][nx+dx] == stone: # 앞에 한칸에 더 있으면
                            break
                        else : win = stone
                        y, x = i, j
                    # 이동 좌표
                    ny += dy
                    nx += dx
if win > 0:
    print(win)
    print(y+1,x+1)
else:
    print(0)