import sys
from collections import deque

input = sys.stdin.readline

def find_way(x, y, d):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    return [x + dx[d], y + dy[d]]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    metrix[x][y] = 0 # 방문처리

    # bfs 시작
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = find_way(x, y, d)

            if 0 <= nx < m and 0 <= ny < n and metrix[nx][ny] == 1:
                metrix[nx][ny] = 0
                queue.append((nx, ny))


# input
t = int(input())

for _ in range(t):
    m,n,k = map(int, input().split())
    metrix = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        metrix[x][y] = 1
    
    worm = 0
    for i in range(m):
        for j in range(n):
            if metrix[i][j] == 1:
                worm += 1
                bfs(i,j)
    print(worm)