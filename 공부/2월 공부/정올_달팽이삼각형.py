N = int(input())
di = [1,0,-1]
dj = [1,-1,0]

k = 0
num = 1
result = [[""]*N for _ in range(N)]


arr = [[-2]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j] = -1
arr[1][1] = 0
i, j = 1, 1

while True:
    if arr[i+di[k]][j+dj[k]] == -1:
        i = i + di[k]
        j = j + dj[k]
        arr[i][j] = num
        num = (num+1)%10
    elif arr[i+di[k]][j+dj[k]] != -1 and arr[i+di[(k+1)%3]][j+dj[(k+1)%3]] != -1:
        break
    else:
        k = (k+1) % 3
for i in range(N):
    for j in range(i+1):
        result[i][j] = str(arr[i+1][j+1])

for i in range(N):
    print(" ".join(result[i]))