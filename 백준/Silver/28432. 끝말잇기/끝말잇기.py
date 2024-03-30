N = int(input())
words = [input() for _ in range(N)]
M = int(input()) 
samples = [input() for _ in range(M)]

idx = words.index("?")

for sample in samples:
    last = sample[::-1][0]
    first = sample[0]

    if sample not in words:
    # N 이 1개 일 때도 확인해야함
        if idx == 0:
            if len(words) == 1 : print(sample)
            elif last == words[idx+1][0]: #?가 처음일 떄
                print(sample)
        elif idx == N-1 and first == words[idx-1][::-1][0]: #마지막일 때
            print(sample)
        elif 0 < idx < N-1 and last == words[idx+1][0] and first == words[idx-1][::-1][0]: #?가 처음-끝 아닐 때
            print(sample)