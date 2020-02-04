<<<<<<< HEAD
# T = int(input())

# for t in range(1,T+1):
#     N = str(input())
#     result = 1
#     sheep = []
#     for i in range(len(N)):
#         if N[i] not in sheep:
#             sheep.append(N[i])
#     sheep_plus = []

#     while len(sheep) != 10:
#         result += 1
#         sheep_plus = str(int(N)*result)
#         for i in range(len(sheep_plus)):
#             if sheep_plus[i] not in sheep:
#                 sheep.append(sheep_plus[i])
#     print("#{0} {1}".format(t,result))

listed = [7, 2 ,5 ,8,6,11,1]
print(set(listed))
=======
T = int(input())

for tc in range(1,T+1):
    N = str(input())
    sheeps = ""
    sheep = []
    k = 1
    while len(sheep) < 10:
        sheeps = str(int(N) * k)
        for idx in range(len(sheeps)):
            if sheeps[idx] not in sheep:
                sheep.append(sheeps[idx])
                sheep.sort()  
        k += 1
    print("#{0} {1}".format(tc, int(N) * (k-1)))
>>>>>>> 7f179d943a5674d72a90e25cfd55ab206e6dd5ec
