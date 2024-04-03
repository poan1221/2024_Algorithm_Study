# 탑 순서의 반대방향 (왼쪽) 으로 레이저 발사
# 탑 높이..가 맞아야 하니까, 자기 숫자보다 큰 애가 받아 줌
# 수신해주는 탑의 index 를 출력해야 함

N = int(input())
tops = list(map(int, input().split()))

# 맨 처음을 넣어주기, index 와 탑 높이
stack = []
stack.append([1, tops[0]])
# 어차피 맨 왼쪽은 수신할 곳이 없음
result = [0]

for i in range(1, N):
    while stack:
        # 수신할 탑이 있다. (stack에 맨 뒤(-1 인덱스)에 탑 높이와 비교)
        if stack[-1][1] >= tops[i]:
            result.append(stack[-1][0])
            stack.append([i + 1, tops[i]])
            break
        else:
            stack.pop()
    # 수신할 곳이 없으면 결과 0
    if not stack:
        result.append(0)
        stack.append([i + 1, tops[i]])

print(*result)