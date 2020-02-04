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