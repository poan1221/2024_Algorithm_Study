from collections import deque


def get_print_num():
    N, M = map(int, input().split())
    docs = deque(list(map(int, input().split())))
    cnt = 0  # 인쇄 순서

    while docs:
        max_num = max(docs)  # 우선순위가 제일 높은 문서
        first = docs.popleft()  # 맨 앞에 순서의 문서
        M -= 1  # 구하는 문서의 순서도 하나씩 땡겨줌

        # 맨 앞이 우선순위가 제일 높으면 바로 인쇄함 > 인쇄 순서 +1
        if max_num == first:
            cnt += 1
            if M < 0:  # 0보다 작은 순서라면 지금 뽑았다는 뜻
                print_num.append(cnt)
                break
        else:
            docs.append(first)  # 맨 뒤로 보냄
            if M < 0:  # 근데 뽑은 게 알고 싶었던 거라면? M 재정의
                M = len(docs) - 1
    return print_num


testCase = int(input())
print_num = []

for _ in range(testCase):
    result = get_print_num()

print(*result)