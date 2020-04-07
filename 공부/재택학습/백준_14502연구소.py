import copy

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def virus(N, M):
    global walled
    q = copy.deepcopy(vplace)
    visit = copy.deepcopy(visited)
    for k in range(3):
        ks = walled.pop()
        ki, kj = ks[0], ks[1]
        visit[ki][kj] = 1
    room = copy.deepcopy(cnt)-3
    while q:
        vi, vj = q.pop(0)
        visited[vi][vj] = 1
        for t in range(4):
            ni = vi + di[t]
            nj = vj + dj[t]
            if 0 <= ni < N and 0 <= nj < M:
                if visit[ni][nj] == 0 and lab[ni][nj] == 0:
                    room -= 1
                    visit[ni][nj] = 1
                    q.append((ni, nj))
    return room

# 3개의 벽을 세우는 경우
def wall(n):
    global walls
    if n == 3:
        tmp2 = copy.deepcopy(tmp)
        walls.append(tmp2)
    else:
        for i in range(N):
            for j in range(M):
                if used[i][j] == 0 and lab[i][j] == 0:
                    used[i][j] = 1
                    tmp.append([i, j])
                    wall(n+1)
                    tmp.pop()
                    used[i][j] = 0

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
used = copy.deepcopy(visited)
vplace = []     # 최소 바이러스 위치
cnt = 0         # 빈칸
walls = []      # 3개의 벽 경우
tmp = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            vplace.append((i, j))
        if lab[i][j] == 0:
            cnt += 1

# 3개의 벽을 세우는 경우를 구하고
# virus 함수로 남는 room를 돌려받는다
# 그 중 최대를 기록한다

wall(0)
'''
while walls:
    walled = walls.pop()
    print(virus(N,M))'''



