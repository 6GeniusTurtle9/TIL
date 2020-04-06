N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
vplace = []     # 최소 바이러스 위치
cnt = 0         # 빈칸
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            vplace.append((i, j))
        if lab[i][j] == 0:
            cnt += 1

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def virus(N, M):
    vi, vj = vplace.pop(0)
