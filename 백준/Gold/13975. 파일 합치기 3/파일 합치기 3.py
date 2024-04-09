# 파일 중 2개씩 합쳐서 임시파일을 만들고 - 반복
# 파일을 합치는 최소 비용
# 정렬 해놓고 최소값부터 빼서 더하기

import sys
from heapq import *

input = sys.stdin.readline
t = int(input())

# 테스트 케이스 만큼..
for _ in range(t):
    k = int(input())
    chapters = list(map(int, input().split()))
    heap = []  # 최소값을 뽑을 리스트를 만들어 준다.
    answer = 0

    for i in range(k):
        heappush(heap, chapters[i])

    while len(heap) > 1:
        x = heappop(heap)
        y = heappop(heap)

        heappush(heap, x + y)
        answer += x + y

    print(answer)
