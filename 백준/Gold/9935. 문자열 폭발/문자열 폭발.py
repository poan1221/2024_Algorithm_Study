string = input()
bomb = input()

stack = []
len = len(bomb)

for i in string:
    stack.append(i)
    if "".join(stack[-len:]) == bomb:
        del stack[-len:]

print("".join(stack)) if stack else print("FRULA")