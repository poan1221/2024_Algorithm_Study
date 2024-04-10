import sys
from collections import Counter

input = sys.stdin.readline


def find_NGEi():
    cnt = Counter(list)

    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and cnt[list[i]] > cnt[list[stack[-1]]]:
            result[stack.pop()] = list[i]
        stack.append(i)
    return result


n = int(input())
list = list(map(int, input().split()))

print(*find_NGEi())
