T = int(input())

for tc in range(1,T+1):
    N = str(input())
    sheeps = ""
    sheep = []
    k = 1
    while len(sheep) < 10:
        sheeps = str(int(N) * k)
        for idx in range(len(sheeps)):
            if sheeps[idx] not in sheep:
                sheep.append(sheeps[idx])
                sheep.sort()  
        k += 1
    print("#{0} {1}".format(tc, int(N) * (k-1)))