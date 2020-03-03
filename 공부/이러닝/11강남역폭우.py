def trapping_rain(buildings):
    rain = 0
    for idx in range(1, len(buildings) - 1):
        idx_l, idx_r = 0, 0
        for il in range(idx, 0, -1):
            if buildings[il] > buildings[idx_l]:
                idx_l = il
        for rl in range(idx + 1, len(buildings)):
            if buildings[rl] > buildings[idx_r]:
                idx_r = rl
        if min(buildings[idx_l], buildings[idx_r]) - buildings[idx] > 0:
            rain += min(buildings[idx_l], buildings[idx_r]) - buildings[idx]
    return rain

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))






