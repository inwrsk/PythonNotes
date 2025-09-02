class Classy:
    def method1(self):
        print('method1')
    def method2(self):
        self.method1()
    def method3():
        print('method3')
    def method4(self):
        self.method3()
obj=Classy()
obj.method2()#method1
# obj.method4()#Classy.method3() takes 0 positional arguments but 1 was given
#that 1 is our object