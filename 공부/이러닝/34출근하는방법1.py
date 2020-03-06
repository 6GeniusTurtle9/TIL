def staircase(n):
    stair_table = []
    # 0과 1번째 계단 가는 방법
    stair_table.append(1)
    stair_table.append(1)
    # 2번째 부터는 n-1과 n-2에서 오는 방법이 있다
    for i in range(2, n+1):
        stair_table.append(stair_table[i-1]+stair_table[i-2])
    return stair_table[n]

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))