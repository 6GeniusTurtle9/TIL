# 진기의 최고급 붕어빵

T = int(input())

for x in range(1,T+1):
    N, M, K = map(int,input().split())
    c_time = list(map(int,input().split()))
    result = "Possible"
    boong = 0
    cust_dict = {}
    for i in range(len(c_time)):
        if c_time[i] in cust_dict:
            cust_dict[c_time[i]] += 1
        else:
            cust_dict[c_time[i]] = 1
    nujuk = 0
    for sec in range(1,101):
        if sec % M == 0:
            boong += K
        for key, val in cust_dict.items():
            if int(key) == sec:
                nujuk += cust_dict[key]
        if boong - nujuk < 0:
            result = "Impossible"
            break
    print("#{0} {1}".format(x,result))     