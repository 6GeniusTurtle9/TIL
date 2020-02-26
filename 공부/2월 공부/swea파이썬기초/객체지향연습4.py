class Circle:
    pi = 3.14
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r**2 * self.pi

c1 = Circle(2)
print("원의 면적: {}".format(c1.area()))