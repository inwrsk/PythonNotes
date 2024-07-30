list=[45,56.0,-23,0,23]
list.sort()
print(list)#[-23, 0, 23, 45, 56.0]
list=[45,56.0,-23,0,23]
print(sorted(list),type(sorted(list)))#[-23, 0, 23, 45, 56.0] <class 'list'>
print(sorted(list,reverse=True))#56.0, 45, 23, 0, -23]
list=['anwar',2,1]
#print(sorted(list)) typeerror