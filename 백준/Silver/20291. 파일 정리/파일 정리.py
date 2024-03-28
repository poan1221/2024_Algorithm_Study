N = int(input())

files = {}
for _ in range(N):
    file_name, extension = input().split('.')
    if extension in files: files[extension] += 1
    else: files[extension] = 1

for key, val in sorted(files.items()): print(f'{key} {val}')