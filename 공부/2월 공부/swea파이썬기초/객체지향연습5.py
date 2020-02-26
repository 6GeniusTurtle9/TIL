class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r1 = Rectangle(4, 5)
print("사각형의 면적: {}".format(r1.area()))