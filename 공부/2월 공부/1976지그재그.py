T = int(input())

for t in range(1,T+1):
    N = int(input())
    result = 0
    for n in range(1, N+1):
        if n % 2 == 0:
            result -= n
        else:
            result += n

    print("#{0} {1}".format(t, result))