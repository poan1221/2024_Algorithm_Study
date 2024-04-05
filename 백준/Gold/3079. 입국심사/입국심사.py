# n 심사대 개수, m 상근이와 친구들 인원, 심사대에서 걸리는 시간이 주어짐
# 전체 심사 시간의 최소값


def search(arr, m):
    # 탐색할 범위 : 전체 심사 시간의 최소값(1)과 최대값(심사시간 최대값 * 인원수)
    # mid 가 되는 게, 평균 시간이 되는 샘
    # 탐색 기준 : 주어진 시간동안 가능한 심사 인원
    left = 1
    right = max(arr) * m

    while left <= right:
        mid = (left + right) // 2

        people = 0  # 심사한 인원 수 초기
        for i in arr:
            # 심사시간 평균값//심사시간 : 시간동안 몇 명이나 지나갓나
            people += mid // i

            if people >= m:  # 전체 인원만큼 심사했으면 끝
                break

        # 심사 인원 수가 전체 인원(심사받아야 하는 수)보다 더 크면 - 시간이 넉넉했던 것 => 심사를 마칠 수 있는 시간
        if people >= m:
            answer = mid
            right = mid - 1
        # 심사 인원 수가 모자라면 심사를 전체 다 못한 것 - 시간 모자름
        else:
            left = mid + 1
    return answer  # 전체를 다 돌고 나면, 심사 가능 시간의 최소시간이 됨


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
t = list(int(input()) for _ in range(n))

print(search(t, m))