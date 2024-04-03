from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

# 집과 치킨집의 위치 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])

result = float("inf")  # 비교를 위한 양의 무한대 최대값

# M개를 골라서 도시 치킨거리를 계산
for chick in combinations(chicken, M):
    city_distance = 0  # 도시 치킨거리 초기값
    for x in house:
        home_distance = float("inf")
        for y in chick:
            home_distance = min(home_distance, abs(x[0] - y[0]) + abs(x[1] - y[1]))
        city_distance += home_distance
    result = min(result, city_distance)

print(result)
