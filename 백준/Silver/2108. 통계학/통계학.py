# n 개의 수 -> 네 가지 통계 값을 구해서....

import sys

input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]

numbers.sort()

# 산술평균
print(round(sum(numbers) / n))

# 중앙값
print(numbers[len(numbers) // 2])

# 최빈값
# 같은 수가 몇 번이나 나오는지 담아주기
cnt = {}
for i in numbers:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

# 가장 많이 나타나는 값을 찾기
max_cnt = max(cnt.values())
# 여러 개일 때를 다져야 해서.. 다시 담아주기
maxlist = []
for i in cnt:
    if max_cnt == cnt[i]:
        maxlist.append(i)

print(maxlist[1] if len(maxlist) >= 2 else maxlist[0])

# 범위
print(max(numbers) - min(numbers))