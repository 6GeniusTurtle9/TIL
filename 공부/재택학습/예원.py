from collections import deque
from itertools import combinations


def bfs(q):
    global time
    visited = set()
    for i in range(M):
        q[i].append(0)
    while q:
        # node = q.pop(0)
        node = q.popleft()
        # node = (i, j, time)
        if node[2] >= time:
            return

        if (node[0], node[1]) in visited:
            continue
        visited.add((node[0], node[1]))
        for i in range(4):
            nx, ny = node[0] + dx[i], node[1] + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if arr[nx][ny] == 0:
                q.append([nx, ny, node[2] + 1])

    t = node[2]
    if len(visited) == N * N - wall:
        if t < time: time = t


dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []  # 바이러스 좌표
wall = 0  # 벽의 수
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            wall = wall + 1
        elif arr[i][j] == 2:
            virus.append([i, j])
            arr[i][j] = 0

# 바이러스
time = 2500  # 50*50
for new in combinations(virus, M):
    queue = deque(new)
    bfs(queue)

if time == 2500:
    print(-1)
else:
    print(time - 1)