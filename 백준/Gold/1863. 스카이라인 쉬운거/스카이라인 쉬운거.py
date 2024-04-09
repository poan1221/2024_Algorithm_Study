import sys
input = sys.stdin.readline
n = int(input())

stack = []
cnt = 0

for _ in range(n):
    h = int(input().split()[1])

    # 스택이 있는데, 이전 높이가 지금 높이보다 크면, 스택에서 뺴주고 빌딩 추가
    while stack and stack[-1] > h:
        stack.pop()
        cnt += 1

    # 스택이 없거나, 있는데 이전과 같은 높이라면 그냥 스택을 쌓기만 함
    if not stack or (stack and stack[-1] != h):
        stack.append(h)

# 아직 남아있는 스택에 대한 건물 추가
while stack:
    # 높이가 있어야 하므로
    if stack[-1] > 0:
        cnt += 1
    stack.pop()

# print(stack)

print(cnt)