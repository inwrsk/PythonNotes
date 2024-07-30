tuple1=('tuple1',)
tuple2=('tuple2',)
tuple3=('tuple3',)
tuple1,tuple2,tuple3=tuple3,tuple2,tuple1
print(tuple1,tuple2,tuple3)#('tuple3',) ('tuple2',) ('tuple1',)
newtuple=tuple2+(100,)
newtuple2=newtuple*2
print(newtuple,newtuple2)#('tuple2', 100) ('tuple2', 100, 'tuple2', 100)
print('tuple2'in tuple2)#True
print('tuple2' in newtuple)#True
print('tuple2' in tuple1)#False