T = int(input())

for t in range(1,T+1):
    line = list(str(input()))
    #반만 비교하면 된다
    result = 1
    for i in range(0,int(len(line)/2)):
        if line[i] != line[-i-1]:
            result = 0
            break

    print("#{0} {1}".format(t, result))