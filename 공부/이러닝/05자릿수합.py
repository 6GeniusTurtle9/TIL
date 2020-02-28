# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    length = len(str(n)) - 1
    if n < 10:
        return n
    else:
        return (n // 10**length) + sum_digits(n - (n//10**length)*10**length)
        # return sum_digits(n//10) + n%10

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))