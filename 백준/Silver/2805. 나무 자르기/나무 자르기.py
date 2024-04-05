# 절단할 수 있는 높이의 최대값 찾기
# 나무의 높이 안에서 이분탐색
# 적어도 M 미터 (기준), 근데 M 미터는 벌목한 나무 길이의 합


def search(arr, m):
    start = 1
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2

        sum_cutting = 0  # 벌목한 전체 길이의 합_초기
        for i in arr:
            if i >= mid:  # 비교값보다 나무가 커야 잘림
                sum_cutting += i - mid  # 잘린 길이를 더해준다.

        # 기준값 m보다 더 크면
        if sum_cutting >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end  # 최대값을 구하는 것이므로


N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(search(trees, M))
