T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    cabbage = [[0]*M for _ in range(N)]
    for k in range(K):
        nj, ni = map(int, input().split())
        cabbage[ni][nj] = 1

    # 4방향으로 1이 이어진 횟수를 기록
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    cnt = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visited[i][j] == 0:
                

