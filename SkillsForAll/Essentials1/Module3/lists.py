x=[2.,'anwar',56,-234.5,False]
x[0]=x[4]#assigning 5th value to the first value
print(x)#[False, 'anwar', 56, -234.5, False]
print('length of the list is:',len(x))#5
del x[2]
print('after deleting x[2]:',x)#[False, 'anwar', -234.5, False]
print('slicing of lists:',x[0:10])#shoots no error gives the values upto its capacity
#[False, 'anwar', -234.5, False]
print('slicing of lists:',x[0:-1])#in slicing of lists x:y xth position to y-1th position
#[False, 'anwar', -234.5]
#negative index
#let list of length 5 then
#0, 1, 2, 3, 4
#-5,-4,-3,-2,-1
#both the indexes are equivalent