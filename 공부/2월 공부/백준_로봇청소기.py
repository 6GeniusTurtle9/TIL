import pprint

def dfs(i, j):
    global cnt, d, clean
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌 / 로봇의 탐색 방향은 -1씩으로
    clean[i][j] = 1  # 청소한 위치 저장
    cnt += 1
    # path.append((i, j, d, cnt))
    for k in range(4):

        if d - 1 < 0:
            d = 3
        else:
            d = d - 1

        di, dj = dir[d]
        ni = i + di
        nj = j + dj

        if room[ni][nj] == 0 and clean[ni][nj] == 0:    # 탐색 후 청소 안한 곳이면 ㄱㄱ
            dfs(ni, nj)

        elif k == 3 and room[ni - 2*di][nj - 2*dj] != 1:  # 4방향 탐색후 청소 할 곳이 없으면서 뒤가 벽이 아니면
            #cnt -= 1    # 후진 하니까 dfs 문 들어갈 때 cnt 상쇄
            return

        elif k == 3 and room[ni - 2*di][nj - 2*dj]:  # 4방향 탐색후 청소 할 곳이 없으면서 뒤가 벽이면!! 종료!
            return



N,  M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
clean = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        clean[i][j] = room[i][j]

# 방의 외곽은 1로 벽 처리가 되어있다.
di, dj = 0, 0
cnt = 0
# path = []
# s.append((c, r))

dfs(c, r)

# print(path)
print(cnt)
