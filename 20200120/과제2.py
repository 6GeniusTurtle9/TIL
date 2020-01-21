#흐름과 제어 -반복


#21차시
grade = [88,30,61,55,95]

for i in range(0,5):
    if grade[i] >= 60:
        print('%d번 학생은 %d점으로 합격입니다.' %(i+1, grade[i]))
    else:
        print('%d번 학생은 %d점으로 불합격입니다.' %(i+1, grade[i]))

#22차시
for i in range(1, 101):
    print(i)        


#24차시
a = []

for i in range(1, 100):
    if i%2 != 0:
        a.append(i)
print(', '.join(repr(i) for i in a))       

#25차시
result = 0

for i in range(1,101):
    if i%3==0:
        result+=i
        
print('1부터 100사이의 숫자 중 3의 배수의 총합: %d' %result)

#26차시
data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a = 0
b = 0
ab = 0
o = 0

for i in range(len(data)):
    if data[i] == 'A':
        a += 1
        i += 1
    elif data[i] == "B":
        b += 1
        i += 1
    elif data[i] == "AB":
        ab += 1
        i += 1
    else:
        o += 1
        i += 1
blood = {'A': a, 'O': o, 'B': b, 'AB': ab}
print(blood)

#27차시
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum_scores = 0
i = 0

while i < len(scores):
    if scores[i] >= 80:
       
        sum_scores += scores.pop(i)
 
    else:
        i += 1

print(sum_scores)


#28차시
# i = 5
# while i !=0:
#     print("*"*i)
#     i -= 1

#29차시
i = 7
n = 0
while i < 0:
    a = str(" ")
    b = str("*")
    print("{0} {1} {0}".format(a*n,b*i))
    i -= 2
    n += 1

# a = []
# for i in range(31):
#     if i % 2 == 1:
#         a.append(i)
# print(a)


# lunch = ['짜장면', '초밥', '삼겹살', '스테이크','라면','샐러드']
# for idx, menu in enumerate(lunch):
#     print(idx, menu)

# classroom = ['손초능', '박지윤', '강찬엽', '성근제', '김보훈', '유세정']    
# class_list = list(enumerate(classroom))
# print(class_list)
# print(type(class_list[0]))