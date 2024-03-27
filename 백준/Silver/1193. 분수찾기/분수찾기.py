num = int(input())
line = 1

#몇 번째 열의 몇 번째 위치인지 확인하기
while num > line:
	num -= line
	line += 1
    
#짝수 일 때
if line % 2 == 0:
	sun = num
	mom = line - num + 1
#홀수 일 때
else:
	sun = line - num +1
	mom = num

print(f'{sun}/{mom}')