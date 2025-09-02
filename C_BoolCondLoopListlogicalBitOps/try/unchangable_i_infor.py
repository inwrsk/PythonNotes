for i in range(10):
    i+=4
    print(i,end=' ')#4 5 6 7 8 9 10 11 12 13 
#i changes to normal for every iteration    
print(i)#13
print()
x=10
for i in range(x):
    print(i,end=' ')#0 1 2 3 4 5 6 7 8 9
    x-=1
print()
print()
#x is also unchangable
x='anwar'
for i in x:
    print(i,end=' ')#a n w a r
    x='123'
print()
print(x)#123
print()
x=[1,2,3]
for i in x:
    print(i,end=' ')#1 3
    if i==1:
        del x[1]
#here we are changing the array
#in the above cases we are not changing the value but only we are changing the variable reference