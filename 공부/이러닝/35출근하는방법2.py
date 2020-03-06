# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    a, b = possible_steps[1], possible_steps[2]
    table = []
    # 0번째, 1번째는 1
    # 뛰기 가능한 범위까지는 1가지 밖에는 없다
    for i in range(0, a):
        table.append(1)
    # 지난 i에서부터 계단 끝까지
    for j in range(a, stairs+1):
        if j >= b:
            table.append(table[j-1]+table[j-a]+table[j-b])
        else:
            table.append(table[j-1]+table[j-a])

    return table[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))