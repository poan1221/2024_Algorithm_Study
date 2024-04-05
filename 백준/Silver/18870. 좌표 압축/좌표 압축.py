# 입력 받은 좌표를 크기순 정렬한 순서를 출력
# 근데 기존 리스트의 순서대로 정렬 번호를 뽑아야 함
# 같은 수가 주어질 수 있으니, set으로 정리하고 정렬하는 게 맞을 것 같음
# 정렬 순서를 딕셔너리에 남아서 다시 뽑아내야?

import sys

input = sys.stdin.readline
N = input()
x_list = list(map(int, input().split()))
set_x = sorted(set(x_list))  # 중복값 없애고 정렬한 리스트를 받음

dic_index = {}
for i in range(len(set_x)):
    # {값 : index} 로 찍히도록 -> 그래야 다시 키로 값을 던져서 순서를 가져올 수 있음
    dic_index[set_x[i]] = i

for i in x_list:
    print(dic_index[i], end=" ")