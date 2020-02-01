T = int(input())

for t in range(1,T+1):
    line = list(str(input()))
    #1~5 이하는 10이후에도 있는지
    #6~10은 그 다음에 있는지
    result = 1
    for i in range(2,6):
        if line[:i-1] == line[i:i+i-1] and line[:i-1] == line[i+i:i+i+i-1]:
            result = i
            break
    if result == 1:
        for i in range(6,11):
            if line[:i-1] == line[i:i+i-1]:
                result = i
                break
    print("#{0} {1}".format(t, result))