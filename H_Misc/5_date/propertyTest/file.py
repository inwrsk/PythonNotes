import myModule
print(myModule.myClass().myFunc)#val
# print(myModule.myClass().myFunc())#str obj is not callable
print(myModule.myClass().myFunc2)#<bound method myClass.myFunc2 of <myModule.myClass object at 0x000002A452E6B940>>
print(myModule.myClass().myFunc2())#myVal2