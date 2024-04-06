def search(x, y):
    # 탐색할 범위 : 승률 z 가 바뀌는  개임 수니까.. x 0 부터... 지금 x 까지
    # 탐색 기준 : 승률 z
    left = 0
    right = x
    z = (y * 100) // x

    # 승률이 안변한다 -> 99% 이상이다
    # answer = 0
    if z >= 99:
        return -1
    else:
        while left <= right:
            mid = (left + right) // 2

            # 추가 게임을 한 승률이 더 높아지면,
            if (y + mid) * 100 // (x + mid) > z:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer  # 최소 몇 판인지


import sys

input = sys.stdin.readline
x, y = map(int, input().split())

print(search(x, y))