# 오아왼위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(n, m):
    q = [0]*n*m # 큐 생성
    visited = [[0]*(m) for _ in range(n)] # visited 생성
    front = rear = -1
    # 시작점 enq
    rare = 0
    done = 0
    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 1:
                rear += 1
                q[rear] = (i, j)
                visited[i][j] = 1   # 시작점 방문표시
                done += 1
            elif tomatoes[i][j] == 0:
                rare += 1
    if rare == 0 and done != 0 : # 모든 토마토가 익은 경우
        return 0
    last = 0
    cnt = 0
    while front != rear :   # 큐가 비어있지 않으면
        front += 1
        i, j = q[front]
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<= ni < n and 0<= nj < m and tomatoes[ni][nj] == 0 and visited[ni][nj] == 0:
                rear += 1
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1
                last = visited[ni][nj]
                cnt += 1
    if rare != cnt: # 처음 안익은 토마토의 개수와 익은 토마토의 개수가 다르면
        return -1
    else:   # 다익었으면
        return last-1


m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]