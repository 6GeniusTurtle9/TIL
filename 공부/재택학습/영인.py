# 왼쪽부터 시계방향 좌표 이동
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
def BFS(x, y, cnt):
    global visited
    visited[x][y] = 1
    Q = []
    Q.append((x, y, cnt))
    while Q:
        x, y, cnt = Q.pop(0)
        if x == ei and y == ej:
            return cnt
        else:
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                    Q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N*N 배열 체스판
    visited = [[0]*N for _ in range(N)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    cnt = 0
    if si == ei and sj == ej:
        print(0)
    else:
        print(BFS(si, sj, cnt))