array=['anwar',19,'shaik',65.324,True]
print(type(map(str,array)),map(str,array))#<class 'map'><map object at 0x000001E16FF6BFA0>
print(list(map(str,array)))#['anwar', '19', 'shaik', '65.324', 'True']
#map(str,array) will not perform any work but it will just returns an object 
#list(map(str,array)) it will perform an operation
#eg:
arr=[1,'anwar',2]
print(map(int,arr))#here no operation is performed#<map object at 0x000001848D46BF70>
#print(list(map(int,arr)))#the operation is performed here so shoots the error
print(array)#['anwar', 19, 'shaik', 65.324, True]
