# 오아왼위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(i, j):
    visited[i][j] = 1
    q = []
    q.append([i, j])
    while q:
        si, sj = q.pop(0)
        for k in range(4):
            ni = si + dx[k]
            nj = sj + dy[k]
            if 0 <= ni < 100 and 0 <= nj < 100 and visited[ni][nj] == 0:
                if maze[ni][nj] == '3':
                    return 1
                elif maze[ni][nj] == '0':
                    visited[ni][nj] = 1
                    q.append([ni, nj])
    return 0
T = 10
for tc in range(1, T+1):
    x = int(input())
    maze = [list(input()) for _ in range(100)]
    visited = [ [0]*100 for _ in range(100) ]
    flag = 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                si, sj = i, j
                flag = 1
                break
        if flag:
            break
    print('#{} {}'.format(tc, bfs(si, sj)))