list=[1,2,3,4,5]
print(type(list))#<class 'list'>
print('__iter__' in dir(list))#True
print('__next__' in dir(list))#False

# def newIter(self):
#     print('__iter__')
#     return self
# list.__iter__=newIter #AttributeError __iter__ is read_only

it=list.__iter__()
print('__iter__' in dir(it))#True
print('__next__' in dir(it))#True
print(it,type(it))#<list_iterator object at 0x000001B549F6BF70> <class 'list_iterator'>

print(it.__next__())#1
print(next(it))#2
print(it.__next__())#3
for i in it:#so we can say every for loop uses iterator
    print(i,end=' ')#4 5
# print(it.__next__())#Error as all the elements completed