# 버스의 최소비용 구하기
import sys
from heapq import *

input = sys.stdin.readline

# 다익스트라 알고리즘
def dijkstra(start):
    heapq =[]
    heappush(heapq, (0, start))
    dist[start] = 0

    while heapq:
        cost, node = heappop(heapq)

        if dist[node] < cost:
            continue

        for nextNode, nextCost in busInfo[node]:
            nextCost += cost

            if nextCost < dist[nextNode]:
                dist[nextNode] = nextCost
                heappush(heapq, (nextCost, nextNode))
                City[nextNode] = node

n = int(input());
m = int(input());

busInfo = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    busInfo[start].append((end, cost))

start, end = map(int, input().split())
# 방문한 도시 체크용 배열
City = [i for i in range(n + 1)]

# 최단거리 초기화
dist = [float("inf")] * (n + 1)

dijkstra(start)
# 최소비용 출력
print(dist[end])

path = [end]
now = end
while now != start:
    now = City[now]
    path.append(now)

print(len(path))
print(' '.join(map(str, path[::-1])))