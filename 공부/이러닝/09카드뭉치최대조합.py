def max_product(left_cards, right_cards):
    maxV = -10000000
    for lc in left_cards:
        for rc in right_cards:
            if lc*rc >= maxV:
                maxV = lc*rc
    return maxV
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))