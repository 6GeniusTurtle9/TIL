def f(n, N, P):
    global tmp, maxV
    if n == N:
        if maxV <= P:
            maxV = P
    else:
        for t in range(N):
            if Pi[t] == 0:
                Pi[t] = 1
                for k in range(Pj[t]):
                    f(n, N, P*arr[t][k])
                Pi[t] = 0


T = int(input())
for tc in range(T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Pi = [0] * N
    Pj = []
    P = 1
    maxV = -1
    for t in range(N):
        Pj.append(len(arr[t]))
    print(Pi, Pj)
    f(0, N, P)
    print(maxV)