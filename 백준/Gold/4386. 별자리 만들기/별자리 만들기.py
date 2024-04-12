# n 개 별, 별사이의 거리가 가중치
# 별자리를 만드는 최소 비용 - mst
# 별자리 -> 가중치가 있는 간선 만들기가 포인트
# 수학적.. 어쩌고가ㅠ

import sys
import math
input = sys.stdin.readline


# 부모찾기
def find(x):
    return x if parent[x] == x else find(parent[x])


# 유니온 찾기
def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b


# 사이클 찾기
def get_cycle(a, b):
    return find(a) == find(b)


# input
n = int(input())
# 별 좌표
stars = []
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

# 간선 리스트 만들기
edges = []
for i in range(n - 1):
    for j in range(i + 1, n):
        # 거리 구하기 (stars[i][0],stars[i][1]) (stars[j][0],stars[j][1]) 사이의 거리 구하기
        dist = math.sqrt(
            (stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2
        )
        edges.append((i, j, dist))

# 부모용 리스트
parent = [i for i in range(n + 1)]

# 가중치로 정렬
edges.sort(key=lambda x: x[2])

# 별자리를 만드는 비용
result = 0
for a, b, c in edges:
    if not get_cycle(a, b):
        union(a, b)
        result += c

print("{:.2f}".format(result))
