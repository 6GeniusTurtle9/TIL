T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    minV, maxV = 100000000000, -1000000
    for i in range(0, N-M+1):
        tmp = 0
        for j in range(i, i+M):
            tmp += nums[j]
        if tmp >= maxV:
            maxV = tmp
        if tmp <= minV:
            minV = tmp
    print("#{} {}".format(tc, maxV - minV))