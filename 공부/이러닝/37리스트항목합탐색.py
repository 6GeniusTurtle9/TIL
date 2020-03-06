# 이러닝 힌트를 본 뒤 풀었음. 해설과 동일

def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    low = 0
    high = len(sorted_list)-1
    while low != high:
        check = sorted_list[low] + sorted_list[high]
        if check == search_sum:
            return True
        elif check < search_sum:
            low += 1
        else:
            high -= 1
    # while문에서 못찾으면
    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))