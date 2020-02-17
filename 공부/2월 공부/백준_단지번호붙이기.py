def dfs(i, j):
    visited[i][j] = 1
    # 주변이 방문을 했고 0일때 개수 저장

N = int(input())
house = [list(input()) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

visited = [[0]*N for _ in range(N)]