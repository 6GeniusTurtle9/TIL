def power(x, y):
    if y == 0:
        return 1

    if y % 2 == 0:
        return power(x*x, y//2)
    else:
        return x * power(x*x, y//2)

'''이러닝 해설
def power(x, y):
    if y == 0:
    return 1
    
    tmp = power(x, y//2)
    
    if y % 2 == 0:
        return tmp * tmp
    else:
        return x * tmp * tmp
'''

# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))