import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cables = [int(input()) for _ in range(n)]

left = 1
right = max(cables)

while left <= right:
    mid = (left + right) // 2
    
    count = 0
    for len in cables:
        count += len // mid
    
    # n 개보다 많이 많들 수 있는지?
    if count >= k:
        left = mid + 1
    else:
        right = mid - 1

print(right)
