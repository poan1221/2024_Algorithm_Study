N, M = map(int, input().split())

table = [input() for _ in range(N)]
coloring = []

for n in range(N - 7):
    for m in range(M - 7):
        w_first = 0
        b_first = 0
        for i in range(n, n + 8):
            for j in range(m, m + 8):
                if (i + j) % 2 == 0:
                    if table[i][j] != "W":
                        w_first += 1
                    else:
                        b_first += 1
                else:
                    if table[i][j] != "W":
                        b_first += 1
                    else:
                        w_first += 1
        coloring.append(w_first)
        coloring.append(b_first)

print(min(coloring))