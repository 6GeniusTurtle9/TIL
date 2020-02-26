class Shape:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

class Square(Shape):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        return self.length * self.length


s2 = Square(3)
print("정사각형의 면적: {}".format(s2.area()))