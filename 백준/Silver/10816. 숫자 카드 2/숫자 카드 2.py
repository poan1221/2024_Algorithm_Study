N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

cnt = {key: 0 for key in M_list}

for num in N_list:
    if num in cnt:
        cnt[num] += 1
        
print(' '.join(str(cnt[i]) for i in M_list))