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
가위는 1 바위는 2 보는 3
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

