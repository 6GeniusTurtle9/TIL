M, N = map(int, input().split())
T = int(input())
garo = [0]
sero = [0]
for tc in range(T):
    tmp1, tmp2 = map(int, input().split())
    if tmp1 == 0:
        sero.append(tmp2)
    else:
        garo.append(tmp2)

garo.sort()
sero.sort()

garo += [M]
sero += [N]

result = []

for i in range(1,len(garo)):
    for j in range(1,len(sero)):
        result.append((garo[i]-garo[i-1])*(sero[j]-sero[j-1]))
print(max(result))