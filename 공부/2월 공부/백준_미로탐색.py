def f(i, j):
    global minV, visit
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    s = []
    s.append((i, j))
    visit[i][j] += 1        # 누적에 플러스 잘 하자 ^^

    while len(s) != 0:
        mi, mj = s.pop()
        if mi == N and mj == M:
            if minV >= visit[mi][mj]:
                minV = visit[mi][mj]
        else:
            for k in range(4):
                ni = mi + di[k]
                nj = mj + dj[k]
                if maze[ni][nj] == '1':
                    if visit[ni][nj] == 0 or visit[ni][nj] > visit[mi][mj] + 1:
                        # 새로 가는 곳 또는, 이번에 방문할 곳 보다 전에 방문 한 곳이 더 최소일 경우
                        s.append((ni, nj))
                        visit[ni][nj] = visit[mi][mj] + 1
                        # 누적을 할 것이기 때문(처음엔 1, 그다음은 2...)


N, M = map(int, input().split())
maze = [[0]*(M+2) for _ in range(N+2)]
for i in range(1, N+1):
    maze[i] = [0] + list(input()) +[0]

visit = [[0]*(M+2) for _ in range(N+2)]
minV = 10000000
cnt = 0

f(1,1)
print(minV)