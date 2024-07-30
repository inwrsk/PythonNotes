class SuperOne:pass
class SuperTwo:pass
class Sub(SuperOne, SuperTwo):pass

print(SuperOne)#<class '__main__.SuperOne'>

print(SuperOne.__bases__)#(<class 'object'>,)
#a class without explicit superclasses points to an object 
print(Sub.__bases__)#(<class '__main__.SuperOne'>, <class '__main__.SuperTwo'>)
print(Sub.__bases__[0].__name__)#SuperOne
print(Sub.__bases__[1].__name__)#SuperTwo
obj=Sub()
#print(obj.__bases__)#AttributeError