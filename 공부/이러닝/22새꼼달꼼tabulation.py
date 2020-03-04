def max_profit(price_list, count):
    table = [0]
    table.append(price_list[1])
    if count > 2:
        for i in range(2, count+1):
            tmp = []
            #table[2]부터 순서대로
            if i < len(price_list):
                tmp.append(price_list[i])
            for j in range(1, i//2 + 1):
                tmp.append(table[i-j]+ table[j])
            table.append(max(tmp))
    return table[count]
# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))