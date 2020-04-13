def wall(cnt):
    if cnt == 3:                                                   # 벽 만들기
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if map[i][j] == 0:
                    map[i][j] = 1
                    wall(cnt + 1)
                    map[i][j] = 0

def bfs():
    global max_result                                           # 안전 영역 최대값

    Map = [[0]*M for _ in range(N)]                             # 배열 카피하기
    for i in range(N):
        for j in range(M):
            Map[i][j] = map[i][j]

    result = 0
    q = []
    for i in range(N):                                          # 바이러스 있는 곳 q 에 입력
        for j in range(M):
            if Map[i][j] == 2:
                q.append((i,j))
    while q:
        a, b = q.pop(0)
        for i in range(4):
            X, Y = a + dir_list[i][0], b + dir_list[i][1]       # 네 방향 탐색
            if 0 <= X < N and 0 <= Y < M:                       # 배열 안에서
                if Map[X][Y] == 0:                              # 네 방향에서 0 인곳이 있으면
                    Map[X][Y] = 2                               # 바이러스를 퍼트리기
                    q.append((X,Y))                             # 바이러스 있는 곳 q 에 입력

    for i in range(N):                                          # 안전 영역 구하기
        for j in range(M):
            if Map[i][j] == 0:
                result += 1
    max_result = max(max_result, result)                        # 안전 영역 최댓값  구하기

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

dir_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
max_result = 0

wall(0)
print(max_result)