# 1이 가장 먼저 나오는 idx를 알고 cnt +1
# 그다음 0이 나오는 idx cnt +1
# 위 과정을 반복하면서 원래의 메모리 값이 나오면 스톱

T = int(input())

for tc in range(1, T+1):
    original = str(input())
    cnt = 0
    if original[0] == "1":
        cnt += 1
    for idx in range(len(original)-1):
        if original[idx] != original[idx+1]:
            cnt += 1
    print("#{0} {1}".format(tc, cnt))


