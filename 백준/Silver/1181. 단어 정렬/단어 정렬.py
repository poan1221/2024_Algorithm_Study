# 중복은 제거
# 길이에 따른 정렬 -> 길이가 같으면 사전  순
# 길이에 맞춰 딕셔너리에 넣어주고 정렬

from collections import defaultdict

n = int(input())
len_word_mapper = defaultdict(set)  # 중복 제거를 위해
for _ in range(n):
    word = input()
    len_word_mapper[len(word)].add(word) # {3: {'but'}} 형태로 들어감

# 단어 길이만 가지는 리스트를 만들어서 정렬 - 길이순 정렬을 시킴
# 정렬은 list 형태만 가능하므로 변환한다.
keys = list(len_word_mapper.keys())
keys.sort()

# 길이순 정렬을 반복문으로 하나씩 사전순 정렬을 시키면서 출력 -> 길이순 정렬하고 그 뒤에 사전순 정렬까지 완료
for key in keys:
    words = list(len_word_mapper[key])
    words.sort()
    for word in words:
        print(word)

