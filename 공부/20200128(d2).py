#1945 간단한 소인수분해

T = int(input())
for j in range(0, T+1):
    N = int(input())
    list_num = [0, 0, 0, 0, 0]
    prime = [2, 3, 5, 7, 11]
    result = []
    for i in range(0, 5):
        while N % prime[i] == 0:
            N = N // prime[i]
            list_num[i] += 1
        result.append(str(list_num[i]))
        
    print("#{0} {1}".format(j+1, " ".join(result)))