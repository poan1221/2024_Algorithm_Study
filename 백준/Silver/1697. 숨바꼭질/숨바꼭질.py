# 위치 이동 방법 x-1, x+1, 2*x
# 최단시간 구하기 -> bfs

import sys
from collections import deque


# BFS 탐색해야하는 좌표
def bfs(idx):

    q = deque()
    q.append(idx)

    while q:
        x = q.popleft()
        # 큐에 들어온 순서대로 제일 앞의 노드를 뽑아서

        # k 위치에 오면 출력
        if x == k:
            print(visited[x])
            break

        for nx in (x - 1, x + 1, 2 * x):
            # 방문하지 않았을 때
            if 0 <= nx < max and not visited[nx]:
                # 이동 횟수 추가 (이전 자리의 이동횟수 + 1)
                visited[nx] = visited[x] + 1
                # 큐에 추가
                q.append(nx)


input = sys.stdin.readline
n, k = map(int, input().split())
max = 100001  # n과 k의 최대값보다 +1
visited = [0] * max

bfs(n)
