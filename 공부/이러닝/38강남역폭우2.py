def trapping_rain(buildings):
    left_list = [0]
    right_list = [0]
    for i in range(1, len(buildings)):
        left_list.append(max(left_list[i-1], buildings[i-1]))
        


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))