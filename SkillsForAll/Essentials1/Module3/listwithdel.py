x=[2.,'anwar',56,-234.5,False]
print(id(x))#1717118957248
y=x
print(x is y)#true
del x[1]
print(id(x))#1717118957248
print(x is y)#true
del x #deleting the variable x not the list
print(id(y))#1717118957248
print(y)#[2.,'anwar',56,-234.5,False]
#error print(x)
x=y=[2.,'anwar',56,-234.5,False]
del x[:-3]
print(y)#56,-234.5,False
del x[:]#deleting all the elements inside the list
print(x,y)#[] []