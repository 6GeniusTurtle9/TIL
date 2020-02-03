T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    Price_A = W * P
    Price_B = Q
    result = 0

    if W > R:
        Price_B += (W-R)*S

    if Price_A < Price_B:
        result = Price_A
    else:
        result = Price_B

    print("#{0} {1}".format(tc,result))