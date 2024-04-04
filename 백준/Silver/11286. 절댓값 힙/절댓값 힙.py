from heapq import *
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    a = int(input())

    if a:
        heappush(heap, (abs(a), a))
        # 절대값, 원래 값 으로 넣기 - 튜플 형태
        # heapq 에 튜플이 삽입될 경우엔, 튜플의 첫 번째 요소가 정렬의 기준이 된다.
    else:
        if heap:
            print(heappop(heap)[1])
            # 원래 값을 출력해야 하므로, [1] 위치 값을 뽑아준다.
        else:
            print(0)
