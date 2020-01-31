# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q2(number):
    """
    아래에 코드를 작성하시오.
    number는 양의 정수로만 구성 되어있습니다.
    number의 각 자리 수의 곱의 결과를 정수로 반환합니다.
    """
    str_num = str(number)
    result = 1
    for i in range(len(str_num)):
        result *= int(str_num[i])
    return result
    
# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q2(123))
    print(q2(2020))
    print(q2(123456789))