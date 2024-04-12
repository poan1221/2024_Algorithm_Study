import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cables = [int(input()) for _ in range(n)]

# n 개보다 많이 많들 수 있는지?
def make_n_cables():
    count = 0
    for len in cables:
        count += len // mid
        if count >= k:
            return True
    return False

left = 1
right = max(cables)

while left <= right:
    mid = (left + right) // 2
    if make_n_cables():
        left = mid + 1
    else:
        right = mid - 1

print(right)