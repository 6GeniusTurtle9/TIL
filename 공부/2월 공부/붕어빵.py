# 진기의 최고급 붕어빵

T = int(input())

for x in range(1,T+1):
    N, M, K = map(int,input().split())
    c_time = list(map(int,input().split()))
    c_time.sort()
    result = "Possible"
    boong = 0
    cust_dict = {}
    for sec in c_time:
        if sec in cust_dict:
            cust_dict[sec] += 1
        else:
            cust_dict[sec] = 1
    nujuk = 0
    for sec in cust_dict:
        nujuk += cust_dict[sec]
        boong = K*(sec//M)      #해당 sec까지 만들어진 붕어빵 수
        if boong < nujuk:
            result = "Impossible"
            break
    print("#{0} {1}".format(x,result))     