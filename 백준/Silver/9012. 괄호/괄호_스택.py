def valid_PS(string):
    temp = []
    for p in string:
        if p == "(":
            temp.append(p)
        elif p == ")":
            if not temp:
                return False
            temp.pop()
    return not temp


n = int(input())

for _ in range(n):
    PS = input()
    print("YES" if valid_PS(PS) else "NO")
