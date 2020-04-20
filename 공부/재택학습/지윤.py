from collections import deque

def bfs(i,j):
    global visited
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        # 8 방향
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        si, sj = q.popleft()
        for k in range(8):
            ni = si + dx[k]
            nj = sj + dy[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if mapp[ni][nj] == 0:
                    visited[ni][nj] = visited[si][sj] + 1
                    q.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 'map' 변수로 쓰지 않게 조심하기
    mapp = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())


    # 시작점 == 목표점 : 이동횟수 0
    if (si, sj) == (ei, ej):
        print('0')
    # 시작점 != 목표점 : bfs 시작
    else:
        bfs(si, sj)
        print(visited[ei][ej]-1)