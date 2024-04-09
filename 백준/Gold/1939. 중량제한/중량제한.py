# n 개의 섬, 두 섬을 잇는 다리, 다리마다 중량제한, 양방향
# 중량의 최댓값을 구해야 - 이분탐색
# 한번에 옮길 수 있는 지 확인 필요 - 무게를 기준으로 bfs?

import sys
from collections import deque


# 일정 무게를 가지고 다리를 건널 수 있는지를 판별
# weight 현재 중량 , 섬정보_q
def bfs(weight):
    queue = deque()
    queue.append(island_one)
    visited = [False] * (n + 1)

    # 섬 방문 처리
    visited[island_one] = True

    # 큐가 비어 있을 때까지 탐색
    while queue:
        # 현재 섬의 정보
        x = queue.popleft()

        # i 연결 섬, w 다리가 가지고 있는 중량제한
        for i, w in bridges[x]:
            # 방문하지 않았고, 현재 다리의 w 이 기준으로 가져온 weight 보다 커야 함
            if not visited[i] and w >= weight:
                # 큐에 추가
                queue.append(i)
                visited[i] = True

    # 두 번째 섬을 방문할 수 있다고 나오면, true 반환
    if visited[island_two]:
        return True
    else:
        return False


input = sys.stdin.readline
n, m = map(int, input().split())
bridges = [[] for _ in range(n + 1)]

for _ in range(m):
    # a 와 b 섬 사이의 연결 + 중량제한 넣어주기
    a, b, c = map(int, input().split())
    bridges[a].append([b, c])
    bridges[b].append([a, c])

# 건너야하는 섬 정보
island_one, island_two = map(int, input().split())

# 무게 기준으로 이분탐색 - 무게 최대값 찾기

start = 1
end = 1000000000

answer = 0

while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        # 옮길 수 있으면, 최대 무게 갱신
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
