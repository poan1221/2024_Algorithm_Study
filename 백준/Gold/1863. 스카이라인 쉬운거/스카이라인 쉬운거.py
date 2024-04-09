# 고도가 바뀌는 지점 x,y
# 건물이 몇 개나 될까.. - 건물은.. y 값이 높아질 때 +1
# stack 으로 비교해가며 넣어야 함 - 정렬 필요

import sys

# from collections import deque

input = sys.stdin.readline
n = int(input())
skyline = list(int(input().split()[1]) for i in range(n))
skyline.append(0)  # 마지막에 0이 아니면 건물이 세어지지 않아서 추가

# 처음부터 높이비교를 하기 위해 임시 값 넣기
stack = [0]
cnt = 0
for h in skyline:
    # 높이 비교를 위해 처음에 담아줌
    height = h
    # 마지막 높이가 지금 높이보다 크면 (즉 라인이 떨어짐)
    while stack[-1] > h:
        # 높이가 기존에 나왔던 높이랑 같으면 안됨
        if stack[-1] != height:
            # 라인이 떨어지는데, 기존 높이랑 같지 않으면 건물
            cnt += 1
            # 비교 높이 갱신
            height = stack[-1]
        # print(f"비교높이 {height}, 지금 높이 {h}")
        stack.pop()
    stack.append(h)

print(cnt)
