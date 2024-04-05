n = int(input())
sources = set(map(int, input().split()))  # 중복값이 없도록 set 으로 받기
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(1 if target in sources else 0)