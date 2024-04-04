# 작은 수의 카드뽑아서 합치고 비교해야 최소한의 비교 수가 됨
# 2개씩 뽑고 더한 값을 다시 리스트에 넣어서 뽑아야 함
# 카드 묶음의 수보다 하나 덜 해야 함 -> 더한 값을 다시 넣고의 과정이므로.

from heapq import *
import sys

input = sys.stdin.readline

N = int(input())
heap = [int(input()) for _ in range(N)]

heapify(heap)
result = 0

for _ in range(N - 1):
    x = heappop(heap)
    y = heappop(heap)

    heappush(heap, x + y)
    result += x + y

print(result)
