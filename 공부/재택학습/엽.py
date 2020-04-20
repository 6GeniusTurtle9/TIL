from itertools import combinations
from copy import deepcopy
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def vi(mapp):
    copymapp = deepcopy(mapp)
    for kk in range(len(v_list)):
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if copymapp[i][j] == 1:
                    visited[i][j] = -1
        queue = []
        for m in range(M):
            queue.append(v_list[kk][m])
            visited[v_list[kk][m][0]][v_list[kk][m][1]] =1
        while queue:
            t = queue.pop(0)
            vi = t[0]
            vj = t[1]
            for k in range(4):
                ni = vi + dx[k]
                nj = vj + dy[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if copymapp[ni][nj] == 0 or copymapp[ni][nj] ==2 :
                        if visited[ni][nj] == 0:
                            queue.append((ni, nj))
                            visited[ni][nj] = visited[vi][vj] + 1
        maxx = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] >= maxx:
                    maxx = visited[i][j]
                elif visited[i][j] == 0:
                    maxx = -1
                    break
            if maxx == -1:
                break
        if maxx == -1 :
            result.append(maxx)
        else:
            result.append(maxx-1)

N, M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 2:
            virus.append([i,j])
v_list = list(combinations(virus,M))
result =[]
vi(mapp)
jinresult = []
for i in range(len(result)):
    if min(result) == -1:
        if result[i] != -1:
            jinresult.append(result[i])
    else:
        jinresult.append(min(result))
if len(jinresult) ==0:
    print(-1)
else:
    print(min(jinresult))