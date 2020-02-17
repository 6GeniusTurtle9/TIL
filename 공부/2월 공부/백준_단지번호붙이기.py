def dfs(i, j):
    global cnt
    if int(house[i][j]) == 0 or visited[i][j] == 1:
        return 0
    else:
        visited[i][j] = 1
        cnt += 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if N-1 >= ni >=0 and N-1 >= nj >= 0:
                if int(house[ni][nj]) == 1 and visited[ni][nj] == 0:
                    if dfs(ni, nj) == 0:
                        return cnt
        return cnt
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
house = [list(input())for _ in range(N)]
visited = [[0]*N for _ in range(N)]
home = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if int(house[i][j]) == 1 and visited[i][j] == 0:
            home.append(dfs(i, j))
home.sort()
print("{}".format(len(home)))
for k in range(len(home)):
    print(home[k], end = "\n")