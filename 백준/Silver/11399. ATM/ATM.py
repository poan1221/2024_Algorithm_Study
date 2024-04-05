# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 -> 돈 뽑는 시간이 작은 사람부터 뽑으면 됨

N = int(input())
line = list(map(int, input().split()))
line.sort()

sum_time = [line[0]]  # 합의 초기값
for i in range(1, N):
    sum_time.append(sum_time[i - 1] + line[i])

print(sum(sum_time))