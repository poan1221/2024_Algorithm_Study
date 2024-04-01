N = int(input())
room = [input() for _ in range(N)]


def find_blank(direction):
    blank = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            point = room[i][j] if direction == "width" else room[j][i]
            if point == ".":
                cnt += 1
                if cnt == 2:
                    blank += 1
            else:
                cnt = 0
                continue
    return blank


width = find_blank("width")
length = find_blank("length")

print(width, length)
