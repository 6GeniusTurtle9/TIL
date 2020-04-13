dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(queue):
    global cnt, result_cnt, front, rear
    while front != rear:
        front += 1
        vi, vj =queue[front]
        for k in range(4):
            ni = vi + dx[k]
            nj = vj + dy[k]
            if 0 <= ni < N and 0 <= nj < M:
                if tomato[ni][nj] == 0 or tomato[ni][nj] ==1:
                    if visited[ni][nj] == 0:
                        rear += 1
                        queue[rear] =(ni, nj)
                        visited[ni][nj] = visited[vi][vj] + 1
                        cnt += 1
                        if visited[ni][nj] >= result_cnt:
                            result_cnt = visited[ni][nj]


M, N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
# 1 익은 토마토 0 익지 않은 토마토 -1 빈칸
visited = [[0]*M for _ in range(N)]
front = -1
rear = -1
queue = [0]*M*N
cnt = 0
result_cnt = 1
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            rear += 1
            queue[rear]=(i,j)
            visited[i][j] = 1
            cnt += 1
        elif tomato[i][j] ==-1:
            visited[i][j] = -1
            cnt += 1
bfs(queue)
if cnt == N*M:
    print(result_cnt-1)
else:
    print(-1)