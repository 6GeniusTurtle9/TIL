def select_stops(water_stops, capacity):
    location = []
    yesman = 0  #장그래 위치
    water = capacity
    while True:
        if yesman + water > water_stops[-1]:
            location.append(water_stops[-1])
            break
        if yesman + water in water_stops:
            yesman += water     #마신 물 만큼 이동
            water = capacity    #물을 최대 용량까지 채움
        else:   # 최대 용량만큼 갔을 때 약수터가 없으면
            water -= 1
            if water == 0:  #갈 곳이 없이 제자리로 오게 된다면
                while True:
                    yesman -= 1
                    if yesman in water_stops:   #뒤로가서 약수터에 도착하면
                        water = capacity    #충전
                        break
        if yesman != 0 and yesman not in location:
            location.append(yesman)
    return location

''' 이러닝 풀이
def select_stops(water_stops, capacity):
    # 약수터 위치 리스트
    stop_list = []

    # 마지막 들른 약수터 위치
    prev_stop = 0

    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]

    # 마지막 약수터는 무조건 간다
    stop_list.append(water_stops[-1])

    return stop_list
'''
# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))