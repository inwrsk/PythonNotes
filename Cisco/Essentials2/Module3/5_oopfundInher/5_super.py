class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."
class Sub(Super):
    def __init__(self, name):
        super().__init__(name)#no need of passing self argument

obj = Sub("Andy")
print(obj)

class Super2:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Is my name " + self.name + "?"
class Sub2(Super2,Super):
    def __init__(self,name1):
        super().__init__(name1)#Super2 is initiated i.e the first in arguments

obj=Sub2('Anwar')
print(obj)
