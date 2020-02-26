class Person():
    def __init__(self,name):
        self.name = name

    def getGender(self):
        return "Unknown"

class Male(Person):
    def __init__(self, name):
        super().__init__(name)

    def getGender(self):
        return "Male"

class Female(Person):
    def __init__(self, name):
        super().__init__(name)

    def getGender(self):
        return "Female"
p1 = Male('Andy')
p2 = Female('Abygale')
print(p1.getGender())
print(p2.getGender())
