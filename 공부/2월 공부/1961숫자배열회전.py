T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    print(arr)

    arr_90 = [[0]*N for _ in range(N)]
    # arr_180 = []
    # arr_270 = []

    for i in range(N):
        for j in range(N):
            arr_90[j][-(1+i)] = arr[i][j]
    print(arr_90)
    row0 = []
    for i in range(N):
        row0.append(str(arr[0][i]))
    row0 += [" "]
    for i in range(N):
        row0.append(str(arr_90[0][i]))
    print("".join(row0))


# 배열을 행으로 뽑는 거
    arr = [list(map(str,input().split()))for _ in range(N)]
    for i in range(N):
        print("".join(arr[i]))