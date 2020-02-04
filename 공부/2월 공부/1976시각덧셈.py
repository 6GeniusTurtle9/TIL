T = int(input())
for tc in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())
    result_m = 0
    bonus_h = 0
    result_h = 0
    if m1 + m2 >= 60:
        result_m = m1 + m2 - 60
        bonus_h = 1
    else:
        result_m = m1 + m2
    if h1 + h2 +bonus_h >12:
        result_h = h1 + h2 +bonus_h - 12
    else:
        result_h = h1 + h2 +bonus_h
    
    print("#{0} {1} {2}".format(tc,result_h,result_m))