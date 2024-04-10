import sys
from heapq import *

input = sys.stdin.readline


def max_heap():
    x = int(input())
    if x > 0:
        heappush(heap, -x)
    else:
        if heap:
            print(-heappop(heap))
        else:
            print(0)


n = int(input())
heap = []
for _ in range(n):
    max_heap()