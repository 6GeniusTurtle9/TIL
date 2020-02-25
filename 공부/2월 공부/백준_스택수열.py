N = int(input())
list_num = []
stack = []
result = []
k = 0
t = 0
maxIdx = 0
flag = 'yes'

for i in range(N):      # 수열 받기
    list_num.append(int(input()))

for idx, val in enumerate(list_num):        # 가능 여부 판단
    if list_num[idx] == N:
        maxIdx = idx
        for i in range(maxIdx, N-1):
            if list_num[i] - list_num[i+1] < 0:
                flag = "NO"
                break
    if flag == 'NO':
        break
#불가능한 경우?
#최대값까지 간 후 내림차순이 아닐 경우
if flag == 'yes':
    for num in range(1,N+1):
        stack.append(num)
        result.append("+")
        while True:
            if stack[-1] == list_num[k]:    #스택 마지막이 수열과 같으면
                stack.pop()
                k += 1
                result.append('-')
                if len(stack) == 0:
                    break
            elif stack[-1] != list_num[k]:
                break
    print("\n".join(result))

else:
    print(flag)