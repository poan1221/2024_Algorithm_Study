import sys

S = sys.stdin.readline().strip()

list = []
for i in range(len(S)):
    for j in range(i,len(S)):
        # print(S[i:j+1])
        list.append(S[i:j+1])

print(len(set(list)))