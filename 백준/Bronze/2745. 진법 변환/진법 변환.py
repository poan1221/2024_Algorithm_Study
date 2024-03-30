N, B = input().split()

base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def change_base(n, b):
    n = n[::-1]
    result = 0
    for idx in range(len(n)):
        result += base.index(n[idx]) * (int(b) ** idx)
    return result

print(change_base(N, B))