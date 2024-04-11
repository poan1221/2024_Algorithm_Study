import sys

input = sys.stdin.readline


# 상위 부모 찾기
def find(x):
    # 나 자신이 부모가 아닐 때 재귀함수로 상위 부모를 찾아감
    return x if parent[x] == x else find(parent[x])


# 부모 찾기_연결 노드간 관계 : 작은 쪽이 부모
def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def get_cycle(a, b):
    return find(a) == find(b)


# 입력 데이터
N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]

# 부모찾기용 집합 선언 _ 0 인덱스는 사용 안함
parent = [i for i in range(N + 1)]

# 간선을 가중치 순으로 정렬
edges.sort(key=lambda x: x[2])

result = 0
for a, b, c in edges:
    if not get_cycle(a, b):
        union(a, b)
        result += c

print(result)
