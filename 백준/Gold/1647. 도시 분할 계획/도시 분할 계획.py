# n 개의 집, m 개의 길, 유지비
# 유지비의 최소합 구하기 - mst

import sys
input = sys.stdin.readline


# 부모찾기
def find(x):
    return x if parent[x] == x else find(parent[x])


# union 찾기
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 사이클 찾기
def get_cycle(a, b):
    return find(a) == find(b)


# 입력 데이터
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(m)]

# 부모찾기용 리스트
parent = [i for i in range(n + 1)]
# 가중치로 정렬
city.sort(key=lambda x: x[2])

# 유지비의 총합 초기값
result = 0
# 과비용 길을 없애기 위해
# 가장 큰 유지비
max_cost = 0

for a, b, c in city:
    if not get_cycle(a, b):
        union(a, b)
        result += c
        max_cost = max(max_cost, c)

print(result - max_cost)
