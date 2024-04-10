import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 0번째 사람(board에서 나 자신) + (n // 2 - 1)명으로 팀 구성
team_with_0s = list(combinations(range(1, n), n // 2 - 1))


# 최소값 비교를 위한 초기값 설정 - 양의 무한대
m = float("inf")

for member in team_with_0s:
    team1 = [0] + list(member)
    team2 = list(set(range(n)) - set(team1))

    # 능력치 초기값
    score1 = 0
    score2 = 0

    # 각 팀의 능력치 구하기_ board 의 각 줄의 수치를 가져와서 더해줌
    for i in range(n // 2):
        for j in range(n // 2):
            score1 += board[team1[i]][team1[j]]
            score2 += board[team2[i]][team2[j]]

    # 능력치의 최소값 구하기
    m = min(m, abs(score1 - score2))

print(m)
