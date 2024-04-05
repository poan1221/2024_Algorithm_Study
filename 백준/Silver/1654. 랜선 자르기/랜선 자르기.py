# 이미 가지고 있는 K개의 랜선을 N개의 랜선으로 자르는 것
# N개를 만들 수 있는 최대 길이를 구하기

n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]
ans = 1 # 정답은 항상 1 이상

# 탐색 범위 설정
# N은 1이상 1,000,000이하의 정수, 랜선의 길이는 2^31-1보다 작거나 같음 -> 1부터 2^31-1 까지..
left = 1
right = 2 ** 31 - 1 # 전선 최대 길이
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid # 전선 길이로 나눈 몫이 만들 수 있는 전선의 개수
        # 전체 cnt : 전체 자른 전선의 개수
    if cnt >= k: # k개 이상의 전선을 만들 수 있으면 정답을 갱신!
        ans = mid
        left = mid + 1 #탐색범위 재설정
    else:
        right = mid - 1
print(ans)