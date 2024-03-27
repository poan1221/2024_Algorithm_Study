import sys
T = int(sys.stdin.readline())

for _ in range(T):
    result = ''
    R, S = sys.stdin.readline().split()
    for i in S:
        result += i * int(R)
    print(result)



