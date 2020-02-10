T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    sum = 0
    t1 = 0
    t2 = 0
    for i in range(N//2):
        for j in range(N//2-t1,N//2+t1+1):
            sum += arr[i][j]
            t1 += 1
        print(sum)
    t2 = t1
    for i in range(N//2+2, N):
        for j in range(N//2-t2, N//2+t2+1):
            sum += arr[i][j]
            t2 -= 1
        print(sum)
    for j in range(N):
        sum += arr[N//2][j]

    print(sum)
