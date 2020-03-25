T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(input())
    check = {}
    maxV, maxN = 0, 0
    for num in nums:
        if num not in check:
            check[num] = 1
        else:
            check[num] += 1
    for key, val in check.items():
        if int(check[key]) >= maxV:
            if int(key) > maxN:
                maxN = int(key)
                maxV = check[key]
    print("#{} {} {}".format(tc, maxN, maxV))
