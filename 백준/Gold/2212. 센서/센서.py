# n 개의 센서, k 개의 집중국 -> 센서를 k 개의 영역으로 나누어 본다
# 수신 길이 합의 최솟값

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# 기지국이 더 많을 때는 거리 0 _ 예외
if k >= n:
    print(0)

else:
    sensor = list(map(int, input().split()))

    # 센서 간의 거리를 알기 위해 정렬
    sensor.sort()

    # 간격을 리스트로 만들어서 제일 간격이 큰 구간에서 잘라질 수 있도록 함
    dist = []
    for i in range(1, n):
        dist.append(sensor[i] - sensor[i - 1])

    # 제일 큰 구간에서 잘리도록 정렬 후 빼주기 - k 구간이 되는 것은 k-1 개로 자름
    dist.sort(reverse=True)
    for _ in range(k - 1):
        dist.pop(0)

    print(sum(dist))