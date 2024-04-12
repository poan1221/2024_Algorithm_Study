# 도시 개수 n, 도로 m, 거리 정보 k, 출발 도시 x
# x 에서 출발하는데, 최단거리가 k 인 도시를 한 줄에 하나씩 오른차순으로 정렬해서 출력
# 그런 도시가 없으면 -1

import sys
from collections import deque

input = sys.stdin.readline


# bfs -  모든 거리가 1 이므로 이게 효율적
def bfs(start):
    distances = [-1] * (n + 1)  # 최단 거리 저장용, -1은 방문하지 않음
    queue = deque([start])
    distances[start] = 0  # 자기자신과는 거리 0

    # print(distances)

    while queue:
        now = queue.popleft()
        dist = distances[now]

        for i in roads[now]:
            if distances[i] == -1:
                # 거리 정보 넣기
                distances[i] = dist + 1
                queue.append(i)

    # 최단 거리가 k 인 도시 찾기
    for i in range(1, n + 1):
        if distances[i] == k:
            result.append(i)

    # 출력
    return result


n, m, k, x = map(int, input().split())
# 도로 정보 표기
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    # print(a, b)
    roads[a].append(b)

# 결과 도시 리스트
result = []

# bfs 실행
bfs(x)

print(*result, sep="\n") if result else print(-1)