def make_list(n, list_name):
    for _ in range(n):
        num = list(map(int, input().split()))
        list_name.append(num)
    return list_name


list_81 = []
make_list(9, list_81)

max_num = max(map(max, list_81))
print(max_num)

for i in range(9):
    for j in range(9):
        if list_81[i][j] == max_num:
            print(i + 1, j + 1)
