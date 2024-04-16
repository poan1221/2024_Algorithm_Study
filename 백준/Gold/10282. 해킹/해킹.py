# 다익스트라 - 가장 짧은 경로 찾기
# 의존성에 따라 다른 컴퓨터들이 감염되는 시간을 구해야

import sys
from heapq import *

input = sys.stdin.readline


def dijkstra(graph, start):
    # 감염 시간_각 노드 간의 거리 저장 리스트 - 무한대로 초기화 후 비교하여 담는다
    distance = [float("inf")] * len(graph)
    distance[start] = 0  # 자기 자신은 0

    # 모든 노드를 저장할 큐 리스트
    # (가중치_감염 시간 , 시작노드)
    queue = [(0, start)]

    while queue:
        cost, node = heappop(queue)

        # 기존 가중치가 더 적으면 무시
        if cost > distance[node]:
            continue

        # 인접한 노드의 가중치를 확인
        for adjNode, next_cost in graph[node]:
            next_cost += cost

            # 현재 노드를 통해 가는 경우가 가중치가 더 적다면, 업데이트
            if next_cost < distance[adjNode]:
                distance[adjNode] = next_cost
                heappush(queue, (next_cost, adjNode))

    # 감염 시간 리스트를 정렬하여, 값을 가져온다 _ 마지막 컴퓨터 감염까지이므로 최대값
    # 0 (시작 자신)이 아니고, 초기값 inf 가 아닌 값으로

    cnt = 0
    last_time = 0
    for time in distance:
        if time < float("inf"):
            cnt += 1
            if time > last_time:
                last_time = time

    return [cnt, last_time]


t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    # 컴퓨터간의 의존성을 담을 리스트 : 0 인덱스는 사용 안 함
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        # b 가 감염되면, a 도 s 시간 후에 감염됨
        graph[b].append([a, s])

    print(*dijkstra(graph, c))