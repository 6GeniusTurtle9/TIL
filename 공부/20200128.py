#2050 알파벳을 숫자로 변환
아스키코드의 번호를 이용한 방법
alphabet = input()
alp_list = list(alphabet)
alp_print = []
for i in range(0, len(alp_list)):
    alp_print.append(str(ord(alp_list[i])-64))
print(" ".join(alp_print))


#2056 연월일 달력
t = int(input())
for i in range(1, t+1):
    cal = input()
    cal_list = list(cal)
    year = int("".join(cal_list[0:4]))
    month = int("".join(cal_list[4:6]))
    day = int("".join(cal_list[6:8]))
    result = 0
    if month <1 or month > 12 or day <1:
        result = -1
    elif month == 2:
        if day > 28:
            result = -1
    elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if day > 31:
            result = -1
    else:
        if day > 30:
            result = -1

    if result == -1:
        print("#{0} {1}".format(i,result))
    else:
        print("#{0} {1:04d}/{2:02d}/{3:02d}".format(i,year,month,day))