def make_list(n, list_name):
    for _ in range(n):
        num = list(map(int, input().split()))
        list_name.append(num)
    return list_name


N, M = map(int, input().split())
A, B = [], []

make_list(N, A)
make_list(N, B)

for i in range(N):
    answer = []
    for j in range(M):
        answer.append(A[i][j] + B[i][j])
    print(*answer)