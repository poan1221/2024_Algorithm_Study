gradeList = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
    }

result, total = 0, 0
for _ in range(20):
    _, score, grade = input().split(' ')
    # print(grade)
    if grade != 'P':
        total += float(score)
        result += float(score) * gradeList[grade]

print(f'{result / total: .6f}')