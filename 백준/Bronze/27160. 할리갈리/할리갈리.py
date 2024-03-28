N = int(input())
card = {}

for _ in range(N):
    S, X = input().split()
    if S in card:
        card[S] += int(X)
    else:
        card[S] = int(X)
print('YES' if 5 in card.values() else 'NO')