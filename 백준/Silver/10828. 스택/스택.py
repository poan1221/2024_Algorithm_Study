import sys
input = sys.stdin.readline

# 입력 데이터
N = int(input())

stack = []
for _ in range(N):
    order = input().split()

    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        print(stack.pop() if stack else -1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        print(1 if not stack else 0)
    elif order[0] == "top":
        print(stack[-1] if stack else -1)