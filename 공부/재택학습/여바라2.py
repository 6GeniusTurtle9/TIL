from itertools import combinations
from copy import deepcopy
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def pan(mapp):
    for kk in range(len(wall)):
        copymapp = deepcopy(mapp)
        for w in range(3):
            copymapp[wall[kk][w][0]][wall[kk][w][1]] = 1
        virus(copymapp,v_list)

def virus(copymapp,v_list):
    visited = [[0]*M for _ in range(N)]
    for j in range(len(v_list)):
        queue = []
        queue.append(v_list[j])
        while queue :
            t = queue.pop(0)
            vi = t[0]
            vj = t[1]
            for k in range(4):
                ni = vi + dx[k]
                nj = vj + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if copymapp[ni][nj] == 0 :
                        if visited[ni][nj] ==0:
                            queue.append((ni, nj))
                            visited[ni][nj] = 1
                            copymapp[ni][nj] = 2
    cnt(copymapp)
def cnt(copymapp):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copymapp[i][j] == 0:
                cnt += 1
    result.append(cnt)

N, M =map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
zero_list=[]
v_list=[]
for i in range(N):
    for j in range(M):
        if mapp[i][j] == 0:
            zero_list.append([i,j])
        elif mapp[i][j] == 2:
            v_list.append([i,j])
wall = list(combinations(zero_list,3))
result = []
pan(mapp)
print(max(result))



