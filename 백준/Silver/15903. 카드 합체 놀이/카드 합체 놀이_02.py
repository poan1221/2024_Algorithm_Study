# n장의 카드에서 x, y를 뽑아 x+y 를 다시 x, y에 넣고 다시 뽑아서 더하고의 반복 m 번
# 구하고자 하는 것은 전체 합이 제일 작을 때
# 힙으로 최소값을 뽑아서 더하면..?

# heapify 로 정렬하기
from heapq import *

n, m = map(int, input().split())
heap = list(map(int, input().split()))  # 최소값을 뽑을 리스트를.. 만들어 준다.
heapify(heap)  # heapq 에 값이 있는 배열을 넣으면 정렬이 필요함

for _ in range(m):
    x = heappop(heap)
    y = heappop(heap)

    heappush(heap, x + y)
    heappush(heap, x + y)

print(sum(heap))
