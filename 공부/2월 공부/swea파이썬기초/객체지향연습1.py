class score:

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math

check = list(map(int,input().split(',')))
test = score(check[0],check[1],check[2])
print("국어, 영어, 수학의 총점: {}".format(test.total()))