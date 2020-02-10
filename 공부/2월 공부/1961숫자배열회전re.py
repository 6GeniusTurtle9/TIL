T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr90 = [[0]*N for _ in range(N)]
    arr180 = [[0]*N for _ in range(N)]
    arr270 =[[0]*N for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            arr90[i][j] = str(arr[-(1+j)][i])
            arr180[i][j] = str(arr[-(1+i)][-(1+j)])
            arr270[i][j] = str(arr[j][-(1+i)])
    print("#{}".format(tc))
    for i in range(N):
        print("{} {} {}".format("".join(arr90[i]), "".join(arr180[i]), "".join(arr270[i])))