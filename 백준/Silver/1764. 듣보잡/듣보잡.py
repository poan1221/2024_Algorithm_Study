N, M = input().split()
no_hear = set(input() for _ in range(int(N)))
no_see = set(input() for _ in range(int(M)))

result = sorted(set(no_hear & no_see))

print(len(result))

for name in result:
    print(name)