import sys
input = sys.stdin.readline


def is_vps():
    stack = []
    for p in VPS_list:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if not stack:
                return print("NO")
            stack.pop()
    return print("YES" if not stack else "NO")


n = int(input())

for _ in range(n):
    VPS_list = input()
    is_vps()