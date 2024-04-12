import sys
from heapq import *

input = sys.stdin.readline

n = int(input())

queue = []
# 각 줄마다 확인하기
for _ in range(n):
    numbers = list(map(int, input().split()))

    if not queue:
        # 없으면, 넣어주기
        for num in numbers:
            heappush(queue, num)
    else:
        for num in numbers:
            # 이미 있으면, 제일 작은 원소와 비교해서 작은 숫자 삭제하고, 큰 숫자 넣어주기
            if num > queue[0]:
                heappushpop(queue, num)  # push, pop 한번에

# 남은 queue는 최종적으로 큰 숫자들 n개_ n번째 큰 수는 그 중 가장 작은 수
print(queue[0])