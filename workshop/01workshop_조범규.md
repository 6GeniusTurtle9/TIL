### 1. 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로 의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

```python
n = int(input())
m = int(input())
garo_list = list(range(n+1))
garo_lenth = len(garo_list)

print(('*'*garo_lenth + '\n')*m)

#print("{0}\n".format("*"n)*m)
```



### 2. print 함수를 한번만 사용해 다음 문장을 출력하시오.

```python
print("\"파일은 C:\\Window\\Users\\내문서\\Python에 저장이 되어있습니다.\" \n 나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'")
```



### 3. 다음과 같은 이차방정식이 있을 때 근을 찾는 수식을 파이썬 코드를 이용하여 출력해보시오.

```python
a = int(input("aX^2 + bX + c의 순서대로 입력하시오."))
b = int(input())
c = int(input())

print(f'{a}X^2 + {b}X + {c}에 대하여')

x1 = (-b + (b*b - 4*a*c)**(1/2)) / (2*a)
x2 = (-b - (b*b - 4*a*c)**(1/2)) / (2*a)

print(f'근 하나는 {x1}이고 다른 하나는 {x2}이다.')
```

