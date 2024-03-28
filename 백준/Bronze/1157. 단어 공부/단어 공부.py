word = input().upper()
word_set = list(set(word))

cnt = []
for i in word_set:
    cnt.append(word.count(i))

max_spell = word_set[cnt.index(max(cnt))]

print('?' if cnt.count(max(cnt)) > 1 else max_spell)