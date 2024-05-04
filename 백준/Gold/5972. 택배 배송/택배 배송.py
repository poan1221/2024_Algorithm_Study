import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start):
    distances = [float("inf")] * (n + 1)
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_cost, u = heapq.heappop(queue)

        if distances[u] < current_cost:
            continue

        for cost, v in graph[u]:
            next_cost = current_cost + cost
            if next_cost < distances[v]:
                distances[v] = next_cost
                heapq.heappush(queue, (next_cost, v))
            
    return distances[n]

print(dijkstra(1))