def valid_PS(string):
    cnt = 0
    for p in string:
        if p == "(":
            cnt += 1
        elif p == ")":
            cnt -= 1
            if cnt < 0:
                return False
    return cnt == 0


n = int(input())

for _ in range(n):
    PS = input()
    print("YES" if valid_PS(PS) else "NO")