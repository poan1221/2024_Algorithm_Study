#요일
weekday = ['SUN','MON','TUE','WED','THU','FRI','SAT']
#2007년 각 달의 일수
days = [31,28,31,30,31,30,31,31,30,31,30,31]
#초기값
day = 0

#m:월, d:일
m, d = map(int, input().split())

#입력된 x월 y일 총 몇 일인지 계산
for i in range(0, m-1):
    day += days[i]

#무슨 요일인지 구하기 : 총 일수는 7로 나눈 나머지값을 요일 리스트에서 구하기
answer = (day+d) % 7
print(weekday[answer])