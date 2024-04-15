import sys
import math

input = sys.stdin.readline


# 부모 찾기
def find(x):
    return x if parent[x] == x else find(parent[x])


# 유니온 찾기
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 사이클 확인하기
def get_cycle(a, b):
    return find(a) == find(b)


# 입력 데이터
N, M = map(int, input().split())

# 우주선 좌표,,, _ 0 인덱스는 안 씀
graph = [0]
for _ in range(N):
    a, b = map(int, input().split())
    graph.append((a, b))

# 간선과 가중치 넣기 -  가중치는 각 우주선들 사이의 거리
edges = []
for i in range(1, len(graph) - 1):
    for j in range(i + 1, len(graph)):
        distance = math.sqrt(
            (graph[i][0] - graph[j][0]) ** 2 + (graph[i][1] - graph[j][1]) ** 2
        )
        edges.append((i, j, distance))

# 간선을 가중치 순으로 정렬
edges.sort(key=lambda x: x[2])


# 부모찾기용 집합 선언 _ 0 인덱스는 사용 안함
parent = [i for i in range(N + 1)]

# 이미 연결된 통로 처리
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)


result = 0
for a, b, c in edges:
    if not get_cycle(a, b):
        union(a, b)
        result += c

# 결과 출력
print(f"{result:.2f}")
