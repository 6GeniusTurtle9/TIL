N = int(input())
result = 0
for tc in range(N):
    check = list(input())
    check_list = []
    cnt = 1
    for i in range(len(check)):
        if check[i] not in check_list:
            check_list.append(check[i])
        elif check[i] != check[i-1]:    # 이미 나온 단어인데 연속이 아님
            cnt = 0
            break
    result += cnt
print(result)