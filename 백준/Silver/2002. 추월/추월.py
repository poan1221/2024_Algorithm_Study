N = int(input())

enter, exit = [input() for _ in range(N)], [input() for _ in range(N)]

crime = 0

for i in range(N):
    if enter[i] != exit[i]: #입출 순서가 다르면 추월
        crime += 1
        before = enter.index(exit[i]) #원래 순서가 어딘지 찾기
        enter.insert(i, enter.pop(before)) # i 위치(추월 위치)로 출입했을 때의 위치를 이동시키기 (빼서 넣기)

print(crime)