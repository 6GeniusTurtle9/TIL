#30차시

# num = int(input())

# num_1 = num%10
# num_10 = num//100
# print(num_1,num_10)


n = 5
m = 9
garo_list = list(range(n+1))
garo_lenth = len(garo_list)

print(('*'*garo_lenth + '\n')*m)



student = {'python' : 80, 'algorithm':99, 'django':89,'flask':83}
sum_score = 0
avg_score = 0
for val in student.values():
    sum_score += val
    avg_score = sum_score/4
print(avg_score)

blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
count_a = 0
count_b = 0
count_o = 0
count_ab = 0
for i in range(len(blood_types)):
    if blood_types[i] == 'A':
        count_a +=1
    elif blood_types[i] == 'B':
        count_b +=1
    elif blood_types[i] == 'O':
        count_o +=1
    else:
        count_ab +=1
b_types = dict(A = count_a, B = count_b, AB = count_ab,O=count_o)
print(b_types)

nums = range(1,51)
odd_num = list(nums)
print(odd_num[0::2])
# print(A[1::2])

student = {'조범규':27, '성근제':28, '박진수':30}
print(student)