n = int(input())

enter_log = {}
for _ in range(n):
    name, log = input().split()
    enter_log[name] = log
    if log == "leave":
        del enter_log[name]
   
print('\n'.join(sorted(enter_log.keys(),reverse=True)))