def dfs(s1, s2):
    global min_cnt, visited
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    stack = []
    stack.append([s1, s2])
    visited[s1][s2] = 1
    while stack:
        a1, a2 = stack.pop()
        if arr[a1][a2] == '3':
            if visited[a1][a2] < min_cnt:
                min_cnt = visited[a1][a2]
        else:
            for dir in range(4):
                ni = a1 + di[dir]
                nj = a2 + dj[dir]
                if arr[ni][nj] != '1':
                    if visited[ni][nj] == 0 or visited[ni][nj] > visited[a1][a2] + 1:
                        stack.append([ni, nj])
                        visited[ni][nj] = visited[a1][a2] + 1


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    s1, s2 = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                s1, s2 = i, j
    visited = [[0] * N for _ in range(N)]
    min_cnt = 2 ** 30 - 1
    dfs(s1, s2)
    if min_cnt == 2 ** 30 - 1:
        print('#{} -1'.format(test_case))
    else:
        print('#{} {}'.format(test_case, min_cnt - 2))