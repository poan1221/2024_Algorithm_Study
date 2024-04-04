from heapq import *

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heap = []  # 최소값을 뽑을 리스트를.. 만들어 준다.

for i in range(n):
    heappush(heap, cards[i])

for _ in range(m):
    x = heappop(heap)
    y = heappop(heap)

    heappush(heap, x + y)
    heappush(heap, x + y)

print(sum(heap))