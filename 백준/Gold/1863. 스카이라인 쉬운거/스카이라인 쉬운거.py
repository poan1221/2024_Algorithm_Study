import sys
input = sys.stdin.readline

def find_min_building():
    stack = []
    buildings = 0

    for h in skyline:
        # 스카이라인이 하강하는 지점 처리: 스택이 비어있지 않고, 현재 높이가 스택의 top보다 낮으면
        while stack and h < stack[-1]:
            stack.pop()
            buildings += 1

        # 스카이라인이 상승하는 지점 또는 같은 높이로 유지되는 경우 스택에 추가
        # 같은 높이의 연속은 중복 추가를 방지하기 위해 처리하지 않음
        if not stack or h > stack[-1]:
            stack.append(h)

    # 스택에 남은 각 상승 지점마다 최소 한 채의 건물이 있음_ 높이가 있는 상황에서만 빌딩 추가
    while stack:
        if stack[-1] > 0:
            buildings += 1
        stack.pop()

    return buildings


n = int(input())
skyline = list(int(input().split()[1]) for _ in range(n))

print(find_min_building())