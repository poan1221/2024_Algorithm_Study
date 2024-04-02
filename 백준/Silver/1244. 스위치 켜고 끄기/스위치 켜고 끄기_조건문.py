N = int(input())
switch = [0] + list(map(int, input().split()))  # 번째에 이미 0이 있도록
M = int(input())

for _ in range(M):
    student, number = map(int, input().split())

    # 남자 일 때 스위치 돌면서 배수이면 바꾸기
    if student == 1:
        for i in range(1, N // number + 1):
            switch[number * i] = 0 if switch[number * i] == 1 else 1
    else:  # 여자 일 때, 양쪽이 같은지 확인
        # 받은 숫자도 변경 해야 함
        switch[number] = 0 if switch[number] == 1 else 1
        i = 1
        while (
            number - i >= 1
            and number + i < N + 1
            and switch[number - i] == switch[number + i]
        ):
            if switch[number - i] == 1:
                switch[number - i] = 0
                switch[number + i] = 0
            else:
                switch[number - i] = 1
                switch[number + i] = 1
            i += 1


for i in range(1, N + 1):
    print(switch[i], end=" ")
    if not i % 20:
        print()
