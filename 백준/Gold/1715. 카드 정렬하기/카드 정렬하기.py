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