x1=3
y1=3
print('x is y',x1 is y1)#x is y True
print('id(x),id(y)',id(x1),id(y1))#same id's
x2='anwar'
y2='anwar'
print('x is y',x2 is y2)#x is y True
print('id(x),id(y)',id(x2),id(y2))#same id's
x3=4.543
y3=4.543
print('x is y',x3 is y3)#x is y True
print('id(x),id(y)',id(x3),id(y3))#same id's
x4=1,2,3
y4=1,2,3
print('x is y',x4 is y4)#x is y True
print('id(x),id(y)',id(x4),id(y4))#same id's
code='''var=3
print(x1 is var)#True
print(id(x1),id(var))#same ids'''
exec(code)
#this works for all the immutable data like int, float, strings, tuples etc because they are unchangable
#mutables like lists donot work in this way because we can modify their values 
list1=[1,2,3]
list2=[1,2,3]
print('list1 is list2', list1 is list2)#list1 is list2 False
print(id(list1),id(list2))#different id's
y='anwar'
x='a'+'nwar'
print(x is y)#True
x=y=[1,2,3]
print(x is y)#True
x.append(1)
print(x,y,x is y)#we are changing the array not dereferencing the variables 