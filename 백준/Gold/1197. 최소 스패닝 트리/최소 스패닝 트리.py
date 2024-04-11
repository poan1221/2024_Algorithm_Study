import sys
from collections import deque

input = sys.stdin.readline


# 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 사이클이 연결되는지 확인 _ 같은 부모를 갖는다면 연결되어 있다.
def get_cycle(parent, a, b):
    return find_parent(parent, a) == find_parent(parent, b)


# 노드 사이의 합집합 찾기 - 더 작은 값이 부모노드로 갱신된다.
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal(vertices, edges):
    # 0 인덱스는 쓰지않고 부모 노드를 찾기 위해 n+1 개 리스트 만들기
    parent = [i for i in range(vertices + 1)]

    # 간선을 가중치 순으로 정렬
    edges.sort(key=lambda x: x[2])

    # 최소 가중치 초기값
    result = 0
    for edge in edges:
        a, b, cost = edge

        # 사이클이 발생하지 않는 경우만 선택하여 간선 연결
        if not get_cycle(parent, a, b):
            union(parent, a, b)
            # 간선의 가중치 더해주기
            result += cost

    return result


# 입력 데이터
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

# 최소 스패닝 트리의 가중치 합 출력
print(kruskal(V, edges))
