T = int(input())
arr = [[0]*102 for _ in range(102)]
for tc in range(1, T+1):
    l, b = map(int, input().split())
    left = l + 1
    bot = b + 1
    for i in range(bot, bot+10):
        for j in range(left, left+10):
             arr[i][j] = 1
cnt = 0
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for i in range(102):
    for j in range(102):
        if arr[i][j] == 1:
            for k in range(4):
                if arr[i+ di[k]][j+ dj[k]] ==0:
                    cnt += 1
print(cnt)