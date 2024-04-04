import sys
from heapq import *

N = int(input())
q = []  # 힙으로 담을 리스트

for _ in range(N):
    # 한 줄 씩
    line = list(map(int, input().split()))

    # q 에 없으면 담고, 있으면 비교한다.
    if not q:
        for num in line:
            heappush(q, num)
    else:
        for num in line:
            if q[0] < num:  # 최소값보다 현재 숫자 크다? 큰 수로 변경해주기
                heappush(q, num)  # 넣어주고
                heappop(q)  # 리스트에서 최소값 빼주고
print(q[0])