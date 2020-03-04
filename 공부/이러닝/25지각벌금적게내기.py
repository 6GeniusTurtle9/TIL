def min_fee(pages_to_print):
    i = len(pages_to_print)
    pages = sorted(pages_to_print)
    result = 0
    for page in pages:
        result += i * page
        i -= 1
    return result

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))