T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    maxV = 0
    maxIdx = 0
    for i in range(N):
        if C[i] > maxV:
            maxV = C[i]
            maxIdx = i+1

    print("#{} {} {}".format(tc, maxIdx, maxV))