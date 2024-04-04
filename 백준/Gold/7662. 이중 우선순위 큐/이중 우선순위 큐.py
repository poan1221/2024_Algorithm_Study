from heapq import *
import sys

input = sys.stdin.readline


tc = int(input())

for _ in range(tc):
    k = int(input())
    max_Q = []
    min_Q = []
    del_Q = [1] * k
    for i in range(k):
        work, num = input().split()
        num = int(num)

        if work == "I":
            heappush(max_Q, (-num, i))
            heappush(min_Q, (num, i))
        else:
            # 원소 삭제 - 삭제했다는 증거를 남기기_ del_Q[i] 값을 0으로 초기화
            if num == 1:
                if max_Q:
                    # 최대값에서 삭제 증거 남기기
                    del_Q[heappop(max_Q)[1]] = 0
            elif num == -1:
                if min_Q:
                    # 최소값에서 삭제 증거 남기기
                    del_Q[heappop(min_Q)[1]] = 0

        # 전체를 다 돌고 나면, 양 쪽 리스트를 맞추기 - 삭제된 값이면 리스트에서도 뺀다
        while min_Q and del_Q[min_Q[0][1]] == 0:
            heappop(min_Q)
        while max_Q and del_Q[max_Q[0][1]] == 0:
            heappop(max_Q)

    print("EMPTY") if not min_Q else print(-max_Q[0][0], min_Q[0][0])
