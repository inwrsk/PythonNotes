x=float('nan')
y=float('-inFinity')
print(x,y)#nan -inf
print(x,type(x))#nan float
if y<x or -y<x or y>x or y>-x:
    print('comparision can be done')
else:
    print('no comparision')#no comparision
if 'a'==float('nan'):
    print('a is not a number')
else:print('nan doesn`t mean comparable to non int`s')#nan doesn`t mean comparable to non int`s
#z=int('inf')=>error