def func(i):
    return i*2
x=map(func,[1,2,3])
print(x,list(x))#<map object at 0x000002B06B26BFD0> [2, 4, 6]
x=map(lambda x:x*3 ,[2,3,4])
print(x,list(x))#<map object at 0x000001C2AE36BE20> [6, 9, 12]