#함수 기초
def greeting(name = "익명"):
    return "{} 안녕 ".format(name)
print(greeting())
print(greeting("범규야"))

def greeting(age, name = "범규"):
    return "{}는 {}살 입니다".format(name,age)
print(greeting(27,"은이"))

print('첫번째 문장',"두번째 문장",end = "//")
print("세번째 문장","네번째 문장",sep="\n")

def my_func(*args):
    return args
print(my_func(1,2,3,4,5,6))
print(my_func(1,2,3,4,5,6)[0])

def my_max(*num):
    result = 0
    for idx, val in enumerate(num):
        if idx == 0:
            result = val
        else:
            if result < val:
                result = val
    return result
print(my_max(1, 3, 4, -5, 3))

#정의되지 않은 키워드 인자를 처리하자
def my_dict(**kwargs):
    result = []

    for key, val in kwargs.items():
        result.append('{0}:{1}'.format(key,val))
    return ", ".join(result)
print(my_dict(한국어 = '안녕', 영어 = 'hi'))
# 인자에 **이번 딕셔너리

#패킹
list(range(3,7))
# =>[3, 4, 5, 6, 7]


#url 만들기
def my_url(key, targetID):
    return "https://naver.com/key={}&targetID={}".format(key,targetID)
print(my_url("keeeey","IIIIIIDDD"))

#problem -control of flow 0
my_str = 'Life is too short, you need python'
def rm_vowels(words):
    vowels = ["a","e","i","o","u"]
    result = []
    for word in words:
        if word not in vowels:
            result.append(word)
    return "".join(result)
print(rm_vowels(my_str))

#딕셔너리 활용
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

fruit_num = 0
nonfruit_num = 0
for key, val in basket_items.items():
    if key in fruits:
        fruit_num += int(val)
    else:
        nonfruit_num += int(val)
print("과일은 {}개이고, {}개는 과일이 아님".format(fruit_num,nonfruit_num))

list_test = ['one', 'two', 'three']
for key, val in enumerate(list_test):
    print(key, val)
tuple_test = ('one', 'two', 'three')
for key, val in enumerate(tuple_test):
    print(key, val)

# dictionary는 items(), keys(), values()를 쓴다
# 나머지 list, set, tuple은 enumerate(뽑을 거)를 쓴다

# 보충
words = ["tiger", "cat", "lion", "mouse"]
short = words[0]
for word in words:
    if len(short)> len(word):
        short = word
print(short)

def contain_same(a, b):
    for char in a:
        if char in b:
            return True
    return False
print(contain_same('my','sweet home'))
print(contain_same('oreo','kikat'))

words = 'Blue bird blue bird lovely blue bird Do not sit on green bean'
def count_w(words):
    result = []
    word_list = list(words.upper().split())
    for i in range(len(word_list)):
        if word_list[i] not in result:
            result.append(word_list[i])
    return len(result)
print(count_w(words))

def bloodtype(bloods):
    result = {}
    abo_type = ["A","B","O","AB"]
    rh_type = ["-","+"]
    for blood in bloods:
        if blood[:-1] in abo_type:
            if blood[:-1] not in result:
                result[blood[:-1]] = 1
            else:
                result[blood[:-1]] += 1
        if blood[-1] in rh_type:
            if blood[-1] not in result:
                result[blood[-1]] = 1
            else:
                result[blood[-1]] += 1
    return result
print(bloodtype(['A+', 'B+', 'A-', 'O-', 'AB+', 'AB-']))

# 월말평가 예시문제
#Q3
def q3(fruits, add, n):
    if add in fruits:
        fruits[add] += n
    else:
        fruits[add] = n
    return fruits
print(q3({'apple': 1}, 'apple', 3))
print(q3({'apple': 1}, 'banana', 1))
print(q3({}, 'apple', 3))