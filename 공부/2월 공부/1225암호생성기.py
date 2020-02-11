for T in range(10):
    tc = int(input())
    password = list(map(int, input().split()))
    result = []
    #pop을 써보자
    k = 1
    while True:
        tmp = password.pop(0) - k
        k += 1
        if k == 6:
            k =1
        if tmp <= 0:
            tmp = 0
            password.append(tmp)
            break
        password.append(tmp)
    for i in range(8):
        result += str(password[i])
    print("#{} {}".format(tc, " ".join(result)))

