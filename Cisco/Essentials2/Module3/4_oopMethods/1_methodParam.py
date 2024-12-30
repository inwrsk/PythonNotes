class Classy:
    def method1():
        x='method1'
        print(x)
    def method2(self):
        y='method2'
        print(y)
print(Classy.__bases__)#(<class 'object'>,)
print(Classy.__base__)#<class 'object'>
obj=Classy()
#obj.method1()#TypeError: Classy.method1() takes 0 positional arguments but 1 was given
obj.method2()#method2
#print(Classy.x)#AttributeError
Classy.method1()#method1
#Classy.method2()#required positional argument: 'self'
#as we discussed earlier you have to pass object