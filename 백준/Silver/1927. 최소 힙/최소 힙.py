from heapq import *
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    a = int(input())
    if a:
        heappush(heap, a)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)