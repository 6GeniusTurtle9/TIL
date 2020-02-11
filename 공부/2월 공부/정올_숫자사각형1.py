n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
k = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = str(k)
        k += 1
for i in range(n):
    print(" ".join(arr[i]))
