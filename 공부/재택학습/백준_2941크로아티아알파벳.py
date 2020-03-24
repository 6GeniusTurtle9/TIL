alps = list(input())
croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
i = 0
cnt = 0

while i < len(alps):
    flag = 0
    for j in range(len(croa)):
        if alps[i] == croa[j][0]:
            if alps[i] == 'd':
                if i + 2 < len(alps) and alps[i+1] == 'z':
                    if alps[i+2] == '=':
                        cnt += 1
                        i += 3
                        flag = 1
                        break
                    else:
                        cnt += 1
                        i += 1
                        flag = 1
                        break
                elif i + 1 < len(alps) and alps[i+1] == '-':
                    cnt += 1
                    i += 2
                    flag = 1
                    break

            elif i + 1 < len(alps) and alps[i+1] == croa[j][1]:
                cnt += 1
                i += 2
                flag = 1
                break
    if flag == 0:
        cnt += 1
        i += 1
print(cnt)