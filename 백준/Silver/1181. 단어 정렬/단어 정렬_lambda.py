# sort 의 key 와 lambda 함수 활용

n = int(input())
words = {input() for _ in range(n)}  # 중복 제거를 위해 set 으로 생성
words = list(words)  # 정렬을 위해 list 로 변환

# 길이 순으로 정렬, 길이가 같다면 사전 순으로 정렬
# 정렬하고자 하는 순서대로 (길이, 사전) 튜플인 형태를 key 로 받아서 정렬함
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
