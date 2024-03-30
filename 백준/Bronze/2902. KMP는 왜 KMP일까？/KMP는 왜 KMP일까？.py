names = input().split('-')
memo = ''

for word in names:
    memo += word[0]
print(memo)