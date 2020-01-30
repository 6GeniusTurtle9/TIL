#function_00

#종합소득세 계산하기
def tax(x):
    if x <= 1200:
        result = x*0.06
    elif x <= 4600:
        result = 1200*0.06 + (x-1200)*0.15
    else:
        result = 1200*0.06 + (4600-1200)*0.15 + (x-4600)*0.35
    return result

#카 쉐어링 요금 계산하기
# 고객의 입장일때
def fee(minute, distance):
    
    m_fee = (minute//10) * 1200 + (minute//30) * 525
    
    if distance > 100:
        d_fee = 100*170 + (distance-100)*85
    else:
        d_fee = distance * 170
        
    result = m_fee + d_fee
    
    return result

#문자열 탐색
def start_end(x):
    count = 0
    for i in x:
        if len(i)>= 2:
            if i[0] == i[-1]:
                count += 1
    return count

#이상한 덧샘
def positive_sum(*x):
    result = 0
    for i in x:
        if i > 0:
            result += i
    return result

#comprhension 버젼
def positive_sums(*x):
    return sum([i for i in x if i > 0])

#Collatz 추측
def collatz(x):
    count = 0
    while x != 1:
        if x % 2 == 0:
            x = x/2
            count += 1
        else:
            x = x*3 + 1
            count += 1
        if count == 500:
            return -1
    return count

#콜라츠 다른 접근
def collatz_2(num):
    # 작업을 500번 반복한다.
    for i in range(500):
        # 주어진 수가 1이 되면 작업 횟수를 return한다.
        if num == 1:
            return i
        # 1이 안되면 짝수, 홀수 조건에 따라 연산
        if num % 2 ==0:
            num = num/2
        else:
            num = num*3 +1
            
        #삼항 연산자
        # num = num/2 if num%2==0 else num*3+1

    # 작업을 500번 반복했는데 1이 되지 않아서 -1 return함
    return -1

#솔로 천국 만들기
def lonely(x):
    result = []
    result.append(x[0])
    
    for i in range(1,len(x)):
        if result[-1] != x[i]:
            result.append(x[i])
    return result

#솔로 또 다른 방법
def lonely_1(numbers):
    # numbers = [1, 1, 3, 3, 0,....]
    result = []
    
    for number in numbers:
        # number -> 1, 1, 3, 3, 0,...
        
        # result 리스트가 비어있는 경우
        if len(result) == 0 :
            result.append(number)
            
        # result 리스트에서 가장 최근에 넣은 요소와 number 값을 비교해서 다른 경우 추가
        if number != result[-1]:
            result.append(number)
            
        return result

# Pythonic

def lonely_2(numbers):
    result = []
    # enumerate는 인덱스와 값을 뽑아줌
    for idx, number in enumerate(numbers):
        # 첫번째 요소면 바로 추가(처음 검사하기 때문에 당연히 비어있는 상태)
        if idx == 0 :
            result.append(number)
            
        if number != result[-1]:
            result.append(number)
            
        return result


#function_01

#abs()
def my_abs(x):
    #1. 들어온 값이 복소수인 경우
    if type(x) == complex:
    #1-1. 복소수 크기 return
        return ((x.real**2 + x.imag**2)**(1/2))
    #2. 들어온 값이 숫자인 경우
    else:
        #2-1. -0.0 이 들어올 수도 있기 때문에
        if x == 0:
            return x**2
        #2-2. 0 보다 작은 경우
        elif x < 0:
            return x * -1
        else:
            return x

# 좀더 깔끔하나 실수형으로 안나옴
def my_abs2(x):
    if type(x) == complex:
        return ((x.reak**2 + x.imag**2)**(1/2))
    return ((x**2)** 0.5)


#all
def my_all(x):
    # x의 길이만큼 참이거나, 길이가 0일때 True
    if len(x) == 0:
        return True
    elif [] in x:
        return False
    else:
        return True

#all 쌤 풀이
def my_all2(elements):
    #1. 모든 요소를 검사한다
    for element in elements:
        #1-1. 요소가 하나라도 비어있으면 (False 찾기)
        # 0은 False, 1이상? 은 True입니다
        if not element:
            return False       
            
    #2-1. 위에서 for 문을 돌지 않은 경우 -> 요소가 비어있음 -> True
    #2-2. 위에서 for 문이 종료됐는데 return False를 만나지 않은 경우 -> 요소가 전부 참 -> True
    return True

#any 쌤 풀이
def my_any(elements):
    #요소 전부 검사
    for element in elements:
        # 요소가 하나라도 값이 있으면(하나라도 True면) -> 최종적으로 True
        if element:
            return True
    #전부 검사했는데 비어있으면(전부 False) -> 최종적으로 False
    return False