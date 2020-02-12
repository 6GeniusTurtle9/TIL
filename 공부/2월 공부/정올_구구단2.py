s, e = map(int, input().split())
if s <= e:
    for t in range(s, e+1):
        for i in range(1, 4):
            if t*i < 10:
                print("{} * {} =  {}".format(t,i,t*i),end="   ")
            else:
                print("{} * {} = {}".format(t, i, t * i), end="   ")
        print()
        for i in range(4,7):
            if t * i < 10:
                print("{} * {} =  {}".format(t, i, t * i), end="   ")
            else:
                print("{} * {} = {}".format(t, i, t * i), end="   ")
        print()
        for i in range(7,10):
            if t*i < 10:
                print("{} * {} =  {}".format(t,i,t*i),end="   ")
            else:
                print("{} * {} = {}".format(t, i, t * i), end="   ")
        print()
        print()
else:
    for t in range(s, e - 1,-1):
        for i in range(1, 4):
            if t * i < 10:
                print("{} * {} =  {}".format(t, i, t * i), end="   ")
            else:
                print("{} * {} = {}".format(t, i, t * i), end="   ")
        print()
        for i in range(4, 7):
            if t * i < 10:
                print("{} * {} =  {}".format(t, i, t * i), end="   ")
            else:
                print("{} * {} = {}".format(t, i, t * i), end="   ")
        print()
        for i in range(7, 10):
            if t * i < 10:
                print("{} * {} =  {}".format(t, i, t * i), end="   ")
            else:
                print("{} * {} = {}".format(t, i, t * i), end="   ")
        print()
        print()
