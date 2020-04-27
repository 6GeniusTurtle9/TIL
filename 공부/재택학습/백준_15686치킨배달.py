from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split()))for _ in range(N)]

house = []
chicken = []
home_chick = []
roads = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
for m in range(1, M+1):
    max_chicken = list(combinations(chicken, m))
    for i in range(len(max_chicken)):
        road = 0    # m개의 치킨집을 뽑았을 때의 거리 합
        for home in house:
            hi, hj = home[0], home[1]
            for j in range(m):
                ci, cj = max_chicken[i][j]
                home_chick.append(abs(ci-hi) + abs(cj-hj))
            road += min(home_chick)
            home_chick = []
        roads.append(road)
print(min(roads))