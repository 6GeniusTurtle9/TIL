T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    minV = 10000000
    last = 0
    for i in range(1, N-1):
        farmer1, farmer2 = 0, 0
        for j in range(0, i+1):
            farmer1 += C[j]
        for j in range(i+1, N):
            farmer2 += C[j]
        if farmer1 >= farmer2 and minV >= farmer1 - farmer2:
            minV = farmer1 - farmer2
            last = i+1
        elif farmer2 > farmer1 and minV >= farmer2 - farmer1:
            minV = farmer2 - farmer1
            last = i+1
    print("#{} {} {}".format(tc, last, minV))
