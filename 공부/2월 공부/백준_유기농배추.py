# 백준에서 런타임 떠서
import sys
sys.setrecursionlimit(1500)


def dfs(i, j):
    if cabbage[i][j] != 1 or visited[i][j] != 0:
        return 0
    else:
        visited[i][j] = 1
        for t in range(4):
            ni = i + di[t]
            nj = j + dj[t]
            if M-1 >= nj >= 0 and N-1 >= ni >= 0:
                if cabbage[ni][nj] == 1 and visited[ni][nj] == 0:
                    if dfs(ni, nj) == 0:
                     return 1
        return 1


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    cabbage = [[0]*M for _ in range(N)]
    for k in range(K):
        nj, ni = map(int, input().split())
        cabbage[ni][nj] = 1

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    visited = [[0]*M for _ in range(N)]
    bug = 0

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visited[i][j] == 0:
                bug += dfs(i, j)

    print(bug)