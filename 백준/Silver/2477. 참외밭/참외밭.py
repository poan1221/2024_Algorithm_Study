import sys

def get_lengths():
    #E=1, W=2, S=3, N=4
    total_list = []
    height_list = []
    width_list = []
    #동서쪽으로 움직이는 경우와 남북쪽으로 움직이는 경우를 나눠서 리스트에 넣어준다.
    for _ in range(6):
        dir, length = map(int, sys.stdin.readline().split())
        total_list.append(length)
        if dir == 1 or dir == 2:
            width_list.append(length)
        else:
            height_list.append(length)
    return total_list, height_list, width_list

#빈 사각형의 한 쪽 길이 구하기
def get_small_length(total, n):
    #최대값의 위치 구하기
    idx = total.index(max(n))
    #위의 인덱스의 양쪽의 값의 차의 절대값
    small_length = abs(total[idx-1] - total[(idx-5 if idx == 5 else idx +1)])
    return small_length

def solution():
    K = int(sys.stdin.readline())

    total, height, width = get_lengths()

    #제일 큰 사각형
    bigbox = max(height) * max(width)

    #작은 사각형의 길이
    small_w, small_h = get_small_length(total, width), get_small_length(total, height)

    area = bigbox - (small_w * small_h)
    return area * K

print(solution())