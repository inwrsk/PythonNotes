#we cannot modify tuples like tuple.append or del tuple or tuple[0]='value'
tuple1=('anwar','shaik',19)
tuple2='shaik',19,'anwar'
tuple3=3,
tuple4=(4,)
print(tuple1,tuple2,tuple3,tuple4)#('anwar', 'shaik', 19) ('shaik', 19, 'anwar') (3,) (4,)
notatuple=(1)
print(notatuple)#1
print('operating tuples')
for element in tuple1:
    print(element,end='_')#anwar_shaik_19_
print()
for i in range(len(tuple1)):
    print(tuple1[i],end='_')#anwar_shaik_19_
print()
print(tuple1[:-1])#('anwar', 'shaik')
