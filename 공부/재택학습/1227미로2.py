def dfs(si, sj):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    stack = []
    stack.append([si, sj])
    visited[si][sj] = 1
    while stack:
        ai, aj = stack.pop()
        if maze[ai][aj] == '3':
            return 1
        else:
            for t in range(4):
                ni = ai + di[t]
                nj = aj + dj[t]
                if maze[ni][nj] != '1' and visited[ni][nj] == 0:
                    stack.append([ni, nj])
                    visited[ni][nj] = 1
    return 0


N = 10
for tc in range(1, N+1):
    testcase = int(input())
    maze = [list(input()) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    result = 0

    si, sj = '0', '0'
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                si, sj = i, j
                break
    result = dfs(si, sj)
    print("#{} {}".format(tc, result))

