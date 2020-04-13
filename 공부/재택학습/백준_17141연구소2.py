import copy

def virus(n):
    global cur_virus
    if n == M:
        tmp2 = copy.deepcopy(tmp)
        cur_virus.append(tmp2)
    else:
        for i in range(len(tmp_virus)):
            if used[i]==0:
                used[i]=1
                tmp.append(tmp_virus[i])
                virus(n+1)
                used[i]=0
                tmp.pop()

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def vtime(N):
    global cur_virus, result, maxkt
    while cur_virus:
        q = copy.deepcopy(cur_virus.pop())
        visit = copy.deepcopy(visited)
        cnt = copy.deepcopy(room)
        while q:
            for _ in range(M):
                k = q.pop()
                # kt 는 1부터 시작하는 퍼지는 시간(결과엔 -1해야함)
                ki, kj, kt = k[0], k[1], k[2]
                visit[ki][kj] = kt
                if kt > maxkt:
                    maxkt = kt
                for t in range(4):
                    ni, nj = ki+di[t], kj+dj[t]
                    if 0<= ni < N and 0<= nj <N:
                        if visit[ni][nj] == 0 and lab[ni][nj] != 1:
                            q.append([ni, nj, kt+1])
                            cnt -= 1
            if cnt == 0:
                if maxkt-1 < result:
                    result = maxkt-1
            if result == 1000000000:
                result = -1
        return result

N, M = map(int, input().split())
lab = [list(map(int, input().split()))for _ in range(N)]
visited = [[0]*N for _ in range(N)]
tmp_virus = []
cur_virus = []
tmp, tmp2 = [], []
room, time, maxkt, result = 0, 1, 0, 1000000000

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            tmp_virus.append([i, j, time])
        elif lab[i][j] == 0:
            room += 1
room += len(tmp_virus) - M
used = [0]*len(tmp_virus)
virus(0)
# M개의 바이러스가 있을 수 있는 위치를 뽑았음
# M개의 바이러스가 위치하지 않는 2는 0으로 만들어서 풀어야함

print(vtime(N))


