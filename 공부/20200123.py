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


print(palindrome("토마토"))