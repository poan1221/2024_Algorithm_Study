# 이분 탐색 방법으로도 풀 수는 있다.
# 메모리 47016 KB / 속도 416 ms


def search(arr, t):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == t:
            return True
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return False


n = int(input())
sources = list(map(int, input().split()))
sources.sort()  # 이분 탐색을 하려면 반드시 정렬되어야 함
m = int(input())
targets = list(map(int, input().split()))
for target in targets:
    print(1 if search(sources, target) else 0)
