#homework day3
#built in 함수

# print(dir(__builtins__))

#오류가 발생하는 코드는?

def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# ssafy(location='대전', name = '철수')
# ssafy('길동', location='광주')
# ssafy(name='허준', '구미')

#답은 3번, 키워드 인자는 먼저 나오면 안됨!

def my_func(a,b):
    c = a + b
    print(c)
result = my_func(4, 7)
print(result)

#workshop day3
def palindrome(word):
    list_word = list(word)
    rev_word = []
    for i in range(1,len(word)+1):
        rev_word.append(list_word[-i])
        
    for j in range(len(word)):
        if rev_word[j] == list_word[j]:
            result = True
        else:
            result = False
    return result    

# 가볍게 하는 법
# def palindrome(word):
#     word[0:len(word):1]
#     word[len(word):0:-1]

# 알고리즘에 집중한 방법
def is_palindrome(word):
    list_word = list(word)
    
    for i in range(len(list_word)//2):      # 0부터 문자열 길이 절반만큼만 반복
        if list_word[i] != list_word[-i-1]: # 왼쪽 문자와 오른쪽 문자가 다르면 False!!!
            return False
    return True                         # for문 반복했는데 다른 글자가 하나도 안나오면 True!!

print(is_palindrome("토마토"))


# control of flow 1

# 구구단
for i in range(2, 10):
    print('------- [{0} 단] -------'.format(i))
    for j in range(1,10):
        print('{0} X {1} = {2}'.format(i,j,i*j))
# 달력
calendar = { 
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 
weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'] 

for month_num in calendar.keys():
    print('         {0} 월'.format(month_num))
    print(" ".join(weeks))
    list_days = list(range(1,calendar[month_num]+1))
    for i in range(0, len(list_days)):
        if (i+1) < 10:
            if (i+1) % 7 == 0:
                print(' {0}'.format(list_days[i]),end="\n")
            else:
                print(' {0}'.format(list_days[i]),end=' ')
        else:
            if (i+1) == list_days[-1]:
                print(list_days[i],end="\n")
            elif (i+1) % 7 == 0:
                print(list_days[i],end="\n")
            else:
                print(list_days[i],end=' ')


# 핸드폰
phone = input("핸드폰 번호를 입력하세요")
if phone == "":
    print("핸드폰번호를 입력하세요")
elif phone[0:3:] != '010':
    print("010부터 핸드폰번호를 입력하세요")
elif len(phone) != 11:
    print("핸드폰번호는 11자리로 입력하세요")
else:
    phone_mask = phone[-4::]
    print("*******{0}".format(phone_mask))         


# 정중앙
word = input()
if len(word) % 2 !=0:
    count = int(len(word)/2)
    print(word[count])
else:
    count = int(len(word)/2)
    print('{0}{1}'.format(word[count-1],word[count]))

# 소수 찾기
numbers = [26, 39, 51, 53, 57, 79, 85]

for number in numbers:
    for x in range(2, number):
        if number % x == 0:
            print('{1} 는 소수가 아닙니다. {0} 는 {1} 의 인수입니다.'.format(x,number))
            break
    else:
        print('{0} 는 소수입니다.'.format(number))