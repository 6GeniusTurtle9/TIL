n = int(input())
m = int(input())
garo_list = list(range(n+1))
garo_lenth = len(garo_list)

print(('*'*garo_lenth + '\n')*m)





print("\"파일은 C:\\Window\\Users\\내문서\\Python에 저장이 되어있습니다.\" \n 나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'")


a = int(input("aX^2 + bX + c의 순서대로 입력하시오."))
b = int(input())
c = int(input())

print(f'{a}X^2 + {b}X + {c}에 대하여')

x1 = (-b + (b*b - 4*a*c)**(1/2)) / 2*a
x2 = (-b - (b*b - 4*a*c)**(1/2)) / 2*a

print(f'근 하나는 {x1}이고 다른 하나는 {x2}이다.')