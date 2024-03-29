N = int(input())

gomgom = set()
cnt = 0

for i in range(N):
    chat = input()
    if chat == "ENTER":
       gomgom = set()
    elif chat != "ENTER" and chat not in gomgom:
        gomgom.add(chat)
        cnt += 1
print(cnt)