import string

N = int(input())
alpha = string.ascii_uppercase
arr = [[" "]*N for _ in range(N)]
k = 0

for j in range(N):
    for i in range(N):
        if j % 2 == 0:
            arr[i][j] = alpha[k]
            k+=1
        else:
            arr[-(1+i)][j] = alpha[k]
            k+=1
        if k > 25:
            k = 0
for i in range(N):
    print(" ".join(arr[i]))