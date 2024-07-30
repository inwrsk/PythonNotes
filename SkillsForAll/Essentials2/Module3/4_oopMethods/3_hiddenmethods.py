class Classy:
    def method(self):
        print('normal method')
    def __hidden(self):
        print('hidden method')
obj=Classy()
obj.method()#normal method
try:
    obj.__hidden()
except:
    print('use _Classy__hidden')#use _Classy__hidden
obj._Classy__hidden()#hidden method