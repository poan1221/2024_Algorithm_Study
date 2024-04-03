N = int(input())

list = list(map(int, input().split()))
result = [-1] * N

stack = []

for i in range(N):
    while stack and list[stack[-1]] < list[i]:
        result[stack.pop()] = list[i]
    stack.append(i)

print(*result)
