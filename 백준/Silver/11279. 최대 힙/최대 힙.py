from heapq import *
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    a = int(input())

    if a:
        heappush(heap, -a)
        # 우선순위를 뒤집어서 넣기 : - 값으로 삽입
    else:
        if heap:
            print(-heappop(heap))
            # - 값 삽입한 것을 상쇄하기 위한, - 다시 붙여주기
        else:
            print(0)