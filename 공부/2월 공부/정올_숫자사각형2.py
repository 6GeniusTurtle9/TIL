n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
k = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            arr[i][j] = str(k)
            k += 1
    if i % 2 == 1:
        for j in range(-1, -(m+1),-1):
            arr[i][j] = str(k)
            k += 1


for i in range(n):
    print(" ".join(arr[i]))
