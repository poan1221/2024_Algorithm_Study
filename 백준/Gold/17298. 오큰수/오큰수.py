import sys
input = sys.stdin.readline

def find_NGE():
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and list[stack[-1]] < list[i]:
            result[stack.pop()] = list[i]
        stack.append(i)
    return result


n = int(input())
list = list(map(int, input().split()))

print(*find_NGE())