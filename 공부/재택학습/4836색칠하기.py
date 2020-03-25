T = int(input())
for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if r1 > r2:
            r1, r2 = r2, r1
        if c1 > c2:
            c1, c2 = c2, c1
        for s in range(r1, r2+1):
            for k in range(c1, c2+1):
                if color == 1 and arr[s][k] != 1:
                    arr[s][k] += 1
                elif color == 2 and arr[s][k] != 2:
                    arr[s][k] += 2
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:
                cnt += 1
    print("#{} {}".format(tc, cnt))
