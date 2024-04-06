# 뿅망치에 맞은 사람의 키 / 2
# 키가 1인 경우에는 줄어들 지 않음 (예외 케이스)
# 횟수 제한 있음
# 횟수 안에 거인의 나라의 모든 거인이 센티보다 키가 작도록 할 수 있는 경우 YES, 최소 사용 횟수 출력
# 다 했는데도 센티보다 키가 크거나 같은 거인이 있으면 NO, 가장 큰 키 출력

import sys
from heapq import *

input = sys.stdin.readline

# 거인나라 인구수, 센티 키, 뿅망치 횟수 제한
n, h, t = map(int, input().split())

titan = []

# 제일 큰 거인을 뽑아야 하므로 최대힙으로 넣음
for _ in range(n):
    heappush(titan, -int(input()))

# 사용 횟수
cnt = 0

for _ in range(t):
    # 키가 1이 아니고, 센티보다 크면?
    if -titan[0] != 1 and -titan[0] >= h:
        heapreplace(titan, -(-titan[0] // 2))
        cnt += 1

# 다 했는데, 여전히 키가 센티보다 크거나 같은 거인이 있으면?
if -titan[0] >= h:
    print("NO")
    print(-titan[0])
else:
    print("YES")
    print(cnt)