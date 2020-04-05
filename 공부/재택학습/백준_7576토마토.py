dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
def bfs(M, N):
    cnt, Mcnt, rare = 0, 0, 0
    q = []
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append([i, j, 0])
                visited[i][j] = 1
            elif tomato[i][j] == 0:
                rare += 1
    if not q:
        return 0
    while q:
        si, sj, cnt = q.pop(0)
        for t in range(4):
            ni, nj = si+dir[t][0], sj+dir[t][1]
            if 0 <= ni < N and 0 <= nj < M:
                if tomato[ni][nj] == 0 and visited[ni][nj] == 0:
                    tomato[ni][nj] = cnt + 1
                    visited[ni][nj] = 1
                    q.append([ni, nj, cnt + 1])
                    rare -= 1
                    if cnt + 1 > Mcnt:
                        Mcnt = cnt + 1
    if rare:
        return -1
    else:
        return Mcnt

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

print(bfs(M, N))





# M, N = map(int, input().split())
# tomato = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# day = 0
# q = []
# dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
#
# for i in range(N):
#     for j in range(M):
#         if tomato[i][j] == 1:
#             q.append([i, j, day])
#
# while q:
#     si, sj, day = q.pop(0)
#     visited[si][sj] = 1
#     result = day
#     for t in range(4):
#         ni = si + dir[t][0]
#         nj = sj + dir[t][1]
#         if 0 <= ni < N and 0 <= nj < M:
#             if tomato[ni][nj] == 0 and visited[ni][nj] == 0:
#                 tomato[ni][nj] = day+1
#                 q.append([ni, nj, day+1])
#
# for i in range(N):
#     for j in range(M):
#         if tomato[i][j] == 0:
#             day = -1
#             break
#     if day == -1:
#         break
# print(day)




# def bfs(M, N):
#     global rare, minD
#     if result <= 0:
#         return result
#     while q:
#         si, sj, day = q.pop(0)
#     for t in range(4):
#         ni = si + dir[t][0]
#         nj = sj + dir[t][1]
#         if 0 <= ni < N and 0 <= nj < M:
#             if tomato[ni][nj] == 0 and visited[ni][nj] == 0:
#                 tomato[ni][nj] = day+1
#                 visited[si][sj] = 1
#                 rare -= 1
#                 q.append([ni, nj, day+1])
#                 if minD <= day + 1:
#                     minD = day+1
#     if rare:
#         return -1
#     else:
#         return minD
#
#
# M, N = map(int, input().split())
# tomato = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# day, minD, check, rare, result = 0, 0, 0, 0, 1
# q = []
# dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
#
# for i in range(N):
#     for j in range(M):
#         if tomato[i][j] == 1:
#             q.append([i, j, day])
#             visited[i][j] = 1
#             check += 1
#         elif tomato[i][j] == 0:
#             rare += 1
# # 토마토가 모두 익은 상태로 시작한다면
# if check == M*N:
#     result = 0
# if not q:
#     result = -1
#
# print(bfs(M,N))
