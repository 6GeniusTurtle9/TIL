def f(i, j, t, m):
    if t == m-1 and arr[i][j] == test[-1]:
        return 1
    else:

        for k in range(4):
            ni = i + d1[k]
            nj = j + d2[k]
            if 0 <= ni <= M-1 and 0 <= nj <= M-1:
                if arr[ni][nj] == test[t] and used[ni][nj] == 0:
                    used[ni][nj] = 1
                    if f(ni, nj, t+1, m) == 1:
                        return 1
                    used[i][j] = 0  # 수열의 의미를 더하기 위함
    return 0

T = int(input())
for tc in range(1, T+1):
    test = list(map(int, input().split()))
    m = len(test)
    N = test.pop(0)
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]
    d1 = [0, 0, 1, -1]
    d2 = [1, -1, 0, 0]
    result = 0

    for i in range(M):
        for j in range(M):
            if arr[i][j] == test[0]:    #시작점이 여러개일 수도..?
                used = [[0]*M for _ in range(M)]    #초기화
                used[i][j] = 1
                result = f(i, j, 1, m)
                if result == 1:
                    break
        if result == 1:
            break
    print("#{} {}".format(tc, result))