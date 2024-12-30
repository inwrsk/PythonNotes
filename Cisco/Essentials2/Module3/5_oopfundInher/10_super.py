class Classy1:
    def __init__(self):
        self.var='Classy1 var'
    def Classy1_func(self):
        print('Classy1 func')

class Classy2:
    def __init__(self):
        self.var='Classy2 var'
    def Classy2_func(self):
        print('Classy2 func')

class subClass(Classy1,Classy2):#CLassy1 is prior than Classy2
    def test__init__(self):
        super().__init__()#super automatically passes self
    def test_func(self):
        super().Classy2_func()

obj=subClass()
print(obj.var)#Classy1 var
obj.test_func()#Classy2 func
#as in the immediate superclass it not having the method searches in the class above it