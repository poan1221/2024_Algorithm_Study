# 변을 공유하지 않아야 함 - 대각선, 아니면 아예 한 칸 떨어져서..
# 그 중 더 큰 것으로 해야하므로, max

import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    n = int(input())
    # 2줄 짜리, n열 배치
    dp = [list(map(int, input().split())) for _ in range(2)]

    # [0,0] [0,1] [0,2] ...
    # [1,0] [1,1] [1,2] ...

    # 1줄 짜리면
    if n == 1:
        print(*max(dp))
    elif n > 1:
        # 1번 인덱스에서 가능한 스티커 점수 넣어주기
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        # 2번부터 n 번까지는 어떤 게 더 큰 지로 계속 더해가기(전의 대각선, 전전의 대각선)
        for i in range(2, n):
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

        # 그 중 더 큰 거 출력하기
        print(max(dp[0][n - 1], dp[1][n - 1]))