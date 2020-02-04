T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    cnt_d = 0
    cnt_e = 0
    while N%2 == 0:
        cnt_a += 1
        N = N//2
    while N%3 == 0:
        cnt_b += 1
        N = N//3
    while N%5 == 0:
        cnt_c += 1
        N = N//5
    while N%7 == 0:
        cnt_d += 1
        N = N//7
    while N%11 == 0:
        cnt_e +=1
    print("#{0} {1} {2} {3} {4} {5}".format(tc,cnt_a,cnt_b,cnt_c,cnt_d,cnt_e))