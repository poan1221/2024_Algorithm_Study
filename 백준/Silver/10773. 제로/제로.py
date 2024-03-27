import sys

k = int(sys.stdin.readline())
final = []

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        final.pop()
    else:
        final.append(n)
    
print(sum(final))
        