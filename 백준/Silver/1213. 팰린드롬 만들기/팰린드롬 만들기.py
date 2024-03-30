from collections import Counter

word = list(map(str, input()))
spell_num = Counter(word)

cnt_odd = 0
for idx in spell_num:
    if spell_num[idx]%2 != 0:
        cnt_odd += 1
        center = idx

harf = ''
word.sort()

if cnt_odd > 1:
    print("I'm Sorry Hansoo")
elif cnt_odd == 0:
    for i in range(0,len(word),2):
        harf += word[i]
    print(harf + harf[::-1])
else:
    word.remove(center)
    for i in range(0,len(word),2):
        harf += word[i]
    print(harf + str(center) + harf[::-1])