class Student:
    def __init__(self, name):
        self.name = name

class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

p1 = Student("홍길동")
p2 = GraduateStudent("이순신", "컴퓨터")

print("이름: {}".format(p1.name))
print("이름: {}, 전공: {}".format(p2.name, p2.major))