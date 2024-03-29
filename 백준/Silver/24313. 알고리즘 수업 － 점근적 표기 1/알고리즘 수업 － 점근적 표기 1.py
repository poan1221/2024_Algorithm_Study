def f(a1, a0, n): return a1*n + a0

def g(n): return n

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(1) if c * g(n0) >= f(a1,a0,n0) and a1 <= c else print(0)