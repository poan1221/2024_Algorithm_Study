# 창고 지붕의 높이 = 제일 높은 기둥의 높이
# 정렬해서 왼쪽부터 높이를 확인해서 더해줘야 함
# 면적 = 가장 높은 기둥을 중심으로 왼쪽에서부터 더해온 값 + 오른쪽에서부터 더해온 값 + 제일 높은 기둥 값

import sys

input = sys.stdin.readline

# 스택 구현
# 가장 높은 기둥을 찾아 일차원 리스트에 추가하는데 인덱스는 가로점으로, 인덱스의 값은 높이로 저장함
# 0부터 최대 가로길이까지 반복문을 나눠서 돈다. 왼쪽 ~ 최대높이 / 오른쪽 ~ 최대높이 높이를 계속 더해준다.
n = int(input())

info = [
    0
] * 1001  # 좌표마다 높이를 넣어줄 배열을 생성. n이 1이상 1000이하이므로 거기에 맞게 만들어줌
max_height = 0  # 기둥의 최대 높이
max_height_idx = 0  # 제일 높은 기둥의 인덱스
end_idx = 0  # 끝 인덱스

# 제일 높은 기둥 찾기
for i in range(n):
    w, h = map(int, input().split())  # 좌표값, 높이
    info[w] = h  # 가로를 인덱스로, 높이를 값으로
    if max_height < h:
        max_height = h
        max_height_idx = w
    end_idx = max(end_idx, w)  # 마지막 가로 위치 갱신

stack = []  # 기둥 높이를 저장할 스택
result = 0  # 결과값

# 첫 인덱스 ~ 제일 높은 기둥까지 넓이를 더해줄 반복문
for i in range(0, max_height_idx + 1):
    if not stack:  # 스택이 비었다면
        stack.append(info[i])  # 현재 높이를 스택에 넣어줌
    else:  # 스택이 비어있지 않다면
        if stack[-1] < info[i]:  # 현재 높이가 스택의 값보다 높다면
            stack.pop()
            stack.append(info[i])  # 스택의 높이 갱신
    result += stack[-1]  # 반복문이 계속될동안 스택에 저장된 높이를 더해준다

# 끝 인덱스 ~ 제일 높은 기둥 직전까지의 넓이를 더해줄 반복문
stack = []  # 기둥 높이를 저장할 스택
for j in range(
    end_idx, max_height_idx, -1
):  # 끝 인덱스부터 제일 높은 기둥 직전까지 -1씩 감소하며 반복
    if not stack:  # 스택이 비었다면
        stack.append(info[j])  # 현재 높이를 스택에 추가
    else:  # 스택이 비지 않았다면
        if stack[-1] < info[j]:  # 현재 높이가 스택의 값보다 높다면
            stack.pop()
            stack.append(info[j])  # 스택의 높이 갱신
    result += stack[-1]  # 반복문이 계속될동안 스택에 저장된 높이 더해줌

print(result)  # 결과값 리턴
