# 창고 지붕의 높이 = 제일 높은 기둥의 높이
# 정렬해서 왼쪽부터 높이를 확인해서 더해줘야 함
# 면적 = 가장 높은 기둥을 중심으로 왼쪽에서부터 더해온 값 + 오른쪽에서부터 더해온 값 + 제일 높은 기둥 값

import sys

input = sys.stdin.readline
n = int(input())

# 기둥을 담은 리스트
h_list = []

for _ in range(n):
    l, h = map(int, input().split())
    h_list.append([l, h])

# 정렬 하기
h_list.sort()

# 제일 높은 기둥 찾기
highest = h_list[0][1]  # 처음 기준
h_idx = 0
for i in range(n):
    # i번째 기둥의 높이가 기준보다 크면
    if h_list[i][1] > highest:
        highest = h_list[i][1]  # 제일 높은 기둥 더 큰 값으로 갱신
        h_idx = i  # 제일 높은 기둥의 인덱스 저장

# 면적 구하기 _ 제일 높은 기둥의 높이를 먼저 면적에 넣어 놓고 시작
area = 0
area = highest

# 왼 -> 기둥까지
# 첫 높이
h = h_list[0][1]
for i in range(h_idx):
    # 다음 기둥의 높이가 지금것보다 높으면 다음 기둥까지만 더하면 됨(갱신 필요)
    if h < h_list[i + 1][1]:
        # 지금 높이*거리를 면적에 더해줌
        area += h * (h_list[i + 1][0] - h_list[i][0])
        # 다음 기둥의 높이로 갱신
        h = h_list[i + 1][1]
    else:
        # 갱신 없이 면적만 더해주기
        area += h * (h_list[i + 1][0] - h_list[i][0])

# 오 -> 기둥 전까지
h = h_list[-1][1]
for i in range(n - 1, h_idx, -1):
    # 다음 기둥의 높이가 지금것보다 높으면 다음 기둥까지만 더하면 됨(갱신 필요)
    if h < h_list[i - 1][1]:
        # 지금 높이*거리를 면적에 더해줌
        area += h * (h_list[i][0] - h_list[i - 1][0])
        # 다음 기둥의 높이로 갱신
        h = h_list[i - 1][1]
    else:
        # 갱신 없이 면적만 더해주기
        area += h * (h_list[i][0] - h_list[i - 1][0])

print(area)
