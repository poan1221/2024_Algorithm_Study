# 풍선 안에는 종이  -N <= 정수 <= N
# 1번부터 터트리는데, 그 다음은 터트린 풍선 안의 종이에 적힌 만큼 이동해서 터트림
# 터진 풍선은 빼고 이동 -> 리스트에서 제거
# 출력은 터진 순서를 index 로 가져와야 하는데, 1부터 시작되어야 함

from collections import deque

N = int(input())
bubbles = deque(enumerate(map(int, input().split()), start=1))
pop_num = []  # 터지는 풍선 번호 담을 리스트

for i in range(N):
    num = bubbles.popleft()  # 맨 앞에꺼를 가져온다.
    pop_num.append(num[0])  # 터지는 풍선의 인덱스를 담아준다.

    # 회전하는 방법으로 이동하는 거라, 방향은 반대로 되어야 함 - 붙이기
    if num[1] > 0:
        # 오른쪽으로 이동이니까, 회전은 반시계 / 터진 풍선 1개 빼주기
        bubbles.rotate(-(num[1] - 1))
    else:
        bubbles.rotate(-num[1])

print(*pop_num)