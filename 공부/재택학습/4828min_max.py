T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    minV, maxV = nums[0], nums[0]
    for i in range(1, N):
        if minV > nums[i]:
            minV = nums[i]
        if maxV < nums[i]:
            maxV = nums[i]
    print("#{} {}".format(tc, maxV-minV))