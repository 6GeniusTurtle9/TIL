T = int(input())
arr = [[0]*101 for _ in range(101)]
cnt = 0
for tc in range(T):
    left, bot = map(int, input().split())
    for i in range(left, left+10):
        for j in range(bot, bot+10):
            arr[i][j] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt +=1
print(cnt)