#  연산자

#7차시
a = int(input())

print('%0.2f inch =>  %0.2f cm' %(a, a*2.54))

#8차시
a=int(input())

print('%0.2f kg =>  %0.2f lb' %(a, a*2.2046))




#흐름과 제어 -if

#17차시
text = input()

if text.islower():
    text_1 = text.upper()
else:
    text_1 = text.lower()
    
print('%s(ASCII: %d) => %s(ASCII: %d)' %(text, ord(text), text_1, ord(text_1)))

#19차시
a=[]

for i in range(100,301):
    if (i // 100) % 2 ==0 and (i // 10) % 2 ==0 and (i % 2) ==0:
        a.append(i)
        
print(','.join(repr(i) for i in a))