#1545 거꾸로 출력

a = int(input())
num = []

for i in range(a,-1,-1):
    num.append(str(i))

print(" ".join(num))

#2019 더블 더블

a = int(input())
num = []

for i in range(0,a+1,1):
    num.append(str(2**i))
    i += 1
print(" ".join(num))

#1936 1대1 가위바위보
#가위는 1 바위는 2 보는 3
a, b = map(int, input().split())
if a != b:
    if a==1 and b==2:
        print("B")
    elif a==1 and b==3:
        print("A")
    elif a==2 and b==1:
        print("A")
    elif a==2 and b==3:
        print("B")
    elif a==3 and b==1:
        print("B")
    else:
        print("A")

#1933 간단한 N의 약수
N = int(input())
num = []
for i in range(1, N+1):
    if N % i == 0:
        num.append(str(i))

print(" ".join(num))

#1938 아주 간단한 계산기
a, b = map(int,input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)

#2025 N줄 덧샘
a = int(input())
a_sum = 0
for i in range(1,a+1):
    a_sum += i
print(a_sum)

#2027 대각선 출력하기
for a in range(0,5):
    print('{0}#{1}'.format("+"*a,"+"*(4-a)))

#2029 몫과 나머지 출력하기
t = int(input())
for i in range(1,t+1):
    a, b = map(int,input().split())
    print("#{0} {1} {2}".format(i,a//b,a%b))

#2043 서랍의 비밀번호
P, K = map(int, input().split())
i = K
count = 1
for i in range(K,999):
    if P == i:
        print(f'{count}')
    else:
        count += 1

#2046 스탬프 찍기
a = int(input())

print("{}".format("#"*a))

#2047 신문 헤드라인
head = input()
head_list = list(head)
result = []

for i in range(0,len(head_list)):
    result.append(head_list[i].upper())

print("".join(result))

#2050 알파벳을 숫자로 변환
alphabet = input()
alp_list = list(alphabet)
alp_dict = {"A":1,"B":2,"C":3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

result = []
for i in range(0, len(alp_list)):
    result.append(str(alp_dict[alp_list[i]]))

print(" ".join(result))

# 2056 연월일 달력
t = int(input())
#for i in (1, t+1):
cal = input()
cal_list = list(cal)
month = []
month_num = 0
day = []
day_num = 0
for i in range(4,6):
    month.append(int(cal_list[i]))
for i in range(6,8):
    day.append(int(cal_list[i]))
#month와 day의 리스트는 추출했으나 숫자로 분석하는 거 실패

#2058 자릿수 더하기
num = input()
num_list = list(num)
result = 0
for i in range(0,len(num_list)):
    result += int(num_list[i])
print(result)

#2063 중간값 찾기
N = int(input())
nums_list = list(map(int, input().split()))
nums_list.sort()
result = nums_list[int(N/2)]
print(result)

#2068 최대수 찾기
T = int(input())
result = 0
num_list = []

for i in range(1,T+1):
    num_list = list(map(int,input().split()))
    result = num_list[0]
    for j in range(1,10):
        if num_list[j] > result:
            result = num_list[j]
    print("#{0} {1}".format(i, result))        

#2070 큰놈, 작은놈, 같은놈
T = int(input())
result = ""

for i in range(1, T+1):
    a, b = map(int,input().split())
    if a > b:
        result = ">"
    elif a < b:
        result = "<"
    else:
        result = "="
    print("#{0} {1}".format(i, result))

#2071 평균값 구하기
T = int(input())
nums_list = []
num_sum = 0
result = 0

for i in range(1, T+1):
    nums_list = list(map(int,input().split()))
    num_sum = 0
    for j in range(0,10):
        num_sum += nums_list[j]
    result = round(num_sum / 10)
    print("#{0} {1}".format(i, result))

#2072 홀수만 더하기
T = int(input())
result = 0
nums_list = []

for i in range(1, T+1):
    result = 0
    nums_list = list(map(int,input().split()))
    for j in range(0, 10):
        if nums_list[j] % 2 == 1:
            result += nums_list[j]
    print("#{0} {1}".format(i, result))