def f(n, P):
    global maxV
    if n == N:
        if maxV <= P:
            maxV = P
        else:
            return
    else:
        for t in range(N):
            if used[t] == 0:
                used[t] = 1
                f(n+1, P*arr[n][t]*0.01)
                used[t] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    maxV = -1
    P = 1
    f(0, P)
    print("#{} {:.6f}".format(tc, maxV*100))