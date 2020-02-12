import string

N = int(input())
alpha = string.ascii_uppercase
arr = [[" "]*N for _ in range(N)]
k = 0
for j in range(N-1, -1, -1):
    for i in range(N-1,-1,-1):
        arr[i][j] = alpha[k]
        k += 1
        if k > 25:
            k = 0
for i in range(N):
    print(" ".join(arr[i]))
