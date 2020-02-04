T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    # min과 제일 작은 것의 idx를 교환, 범위 축소

    min_num = num_list[0]
    min_idx = 0
    for min in range(0,N-1):
        min_num = num_list[min]
        for i in range(min, N):
            if min_num >= num_list[i]:
                min_idx = i
                min_num = num_list[min_idx]
        num_list[min],num_list[min_idx] = num_list[min_idx],num_list[min]
    result = []
    for i in range(N):
        result.append(str(num_list[i]))



    print("#{0} {1}".format(tc," ".join(result)))