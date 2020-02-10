s, e = map(int, input().split())
if s>9 or s<2 or e>9 or e<2:
    print("INPUT ERROR!")
if s >= e:
    for i in range(1, 10):
        for j in range(s, e-1, -1):
            if j*i <10:
                print("{} * {} =  {}".format(j, i, j * i), end="   ")
            else:
                print("{} * {} = {}".format(j, i, j*i), end="   ")
        print()
else:
    for i in range(1,10):
        for j in range(s, e+1):
            if j*i <10:
                print("{} * {} =  {}".format(j, i, j * i), end="   ")
            else:
                print("{} * {} = {}".format(j, i, j*i), end="   ")
        print()