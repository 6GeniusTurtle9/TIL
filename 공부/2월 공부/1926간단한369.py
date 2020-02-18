N = int(input())
game = list(range(1, N+1))
rule = [3, 6, 9]
for num in game:
    cnt = 0
    if num >= 1000:
        print(num, end = ' ')
    elif num >= 100:
        if num // 100 in rule:
            cnt += 1
        if num // 10 - (num // 100)*10 in rule:
            cnt += 1
        if num - (num // 10)*10 in rule:
            cnt += 1
        if cnt == 0:
            print(num, end = ' ')
        else:
            print("{}".format('-'*cnt), end = ' ')
    elif num > 10:
        if num // 10 in rule:
            cnt += 1
        if num - (num // 10)* 10 in rule:
            cnt += 1
        if cnt == 0:
            print(num, end = ' ')
        else:
            print('{}'.format('-'*cnt), end = ' ')
    else:
        if num not in rule:
            print(num, end = ' ')
        else:
            print('-', end = ' ')