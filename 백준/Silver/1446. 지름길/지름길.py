import sys
from heapq import *

input = sys.stdin.readline

def dijkstra(start):
    distances[start] = 0  # 자기자신과는 거리 0

    # (거리, 노드)로 heap 저장
    queue = [(0, start)]
    # print(distances)

    while queue:
        dist, now = heappop(queue)

        # 이미 처리된 노드인 경우에는 건너뛰기
        if dist > distances[now]:
            continue

        for i in graph[now]:
            # 가중치 비교 하기
            cost = dist + i[1]
            # 기존의 최단 경로보다 짧은 경로를 찾은 경우
            if cost < distances[i[0]]:
                # 거리 정보 넣기
                distances[i[0]] = cost
                heappush(queue, (cost, i[0]))

                
n, d = map(int, input().split())

# 도로 정보 _ 직진 + 지름길
graph = [[] for _ in range(d + 1)]
for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, end, lengths = map(int, input().split())
    # 가려는 거리보다 지름길이 길면 고려 안해도 됨
    if end > d:
        continue
    graph[start].append((end, lengths))

# 최단거리 초기화
distances = [float("inf")] * (d + 1)

dijkstra(0)

print(distances[d])
