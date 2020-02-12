import pprint

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[-1]*(N+2) for _ in range(N+2)]

    for a in range(1, N+1):
        for b in range(1, N+1):
            arr[a][b] = 0
    pprint.pprint(arr)

    result = [[0]*N for _ in range(N)]
    visit = [[-1]*(N+2) for _ in range(N+2)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    i, j = 1, 1
    arr[1][1] = 1
    visit[1][1] = 0
    k = 0
    num = 2

    while num <= N**2:
        if arr[i+di[k]][j+dj[k]] == -1 or visit[i+di[k]][j+dj[k]] == 0:
            k += 1
            if k >3:
                k =0
        else:
            i = i + di[k]
            j = j + dj[k]
            arr[i][j] = num
            visit[i][j] = 0
            num += 1
    print("#{}".format(tc))
    for a in range(1, N+1):
        for b in range(1, N+1):
            result[a-1][b-1] = str(arr[a][b])
    for a in range(N):
        print(" ".join(result[a]))