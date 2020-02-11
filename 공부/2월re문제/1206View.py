T = 10
for tc in range(1, T+1):
    case_len = int(input())
    apart = list(map(int, input().split()))
    cnt = 0
    for i in range(2, case_len-2):
        tmp = max(apart[i-2], apart[i-1], apart[i+1], apart[i+2])
        if apart[i] - tmp > 0:
            cnt += apart[i] - tmp
    print("#{} {}".format(tc, cnt))