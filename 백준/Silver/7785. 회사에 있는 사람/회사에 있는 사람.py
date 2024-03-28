n = int(input())

logs = {}
for _ in range(n):
    name, log = input().split()
    logs[name] = log
    if log == "leave":
        del logs[name]
   
for key in sorted(logs,reverse=True): print(key)
