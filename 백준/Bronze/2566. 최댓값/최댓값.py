table = [list(map(int, input().split())) for _ in range(9)]

max_num = max(map(max, table))
print(max_num)

for i in range(9):
    for j in range(9):
        if table[i][j] == max_num:
            print(i + 1, j + 1)