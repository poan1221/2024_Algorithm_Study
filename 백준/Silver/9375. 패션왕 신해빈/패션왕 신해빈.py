# 같은 종류의 의상은 하나만 가능 -> 같은 종류인지로 나눠서 담아야 함
# 의상의 이름과 종류가 들어옴 - 딕셔너리에 담아서 구분

tc = int(input())

for _ in range(tc):
    n = int(input())

    clothes = {}
    for i in range(n):
        name, type = input().split()

        # 의상 종류에 따라 가짓수를 담아주기
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1

    wears = 1
    for i in clothes:  # i 는 key (의상 타입)
        wears *= clothes[i] + 1  # 안 입은 것도 포함해서 계산
    print(wears - 1)  # 아무것도 안 입은 알몸 상태는 빼주기