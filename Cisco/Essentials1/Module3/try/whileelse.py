i=0
while True:
    i+=1
    print(i)
    if i==5:break
else:print(i*20)#else won't work if loop breaks
print(i*10)#50
print('__________')
i=0
while i<4:
    i+=1
    print(i)
    if i==5:break
else:
    print(i*20)#80
    i=1000
print(i*10)#10000

print('___________')
x=[1,2,3,4,5]
while x:
    print(x)
    del x[-1]
'''
[1, 2, 3, 4, 5]
[1, 2, 3, 4]
[1, 2, 3]
[1, 2]
[1]
'''
