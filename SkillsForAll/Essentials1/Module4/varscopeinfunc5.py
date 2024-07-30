def func(list1):
    list1[0]='inside'
    #here you are modifying the list1 which is pointing to ['anwar'] this is affected globally
    del list1#jst deleting the variable
    print('list2',list2)#['inside']
list2=['outside']
func(list2)
print(list2)#['inside']