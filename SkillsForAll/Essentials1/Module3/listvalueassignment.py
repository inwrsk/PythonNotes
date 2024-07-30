list1=['anwar',34,True]
list2=list1[:]#we are assigning the values only
list1[1]='xyz'
print(list1)#['anwar', 'xyz', True]
print(list2)#['anwar', 34 , True]
#list1 is refering new list while list2 isn't
list1=['anwar',34,True]
list2=list1#both are same pointing to same lists
list1[1]='xyz'#modifying the list not dereferencing them
print(list1)#['anwar', 'xyz', True]
print(list2)#['anwar', 'xyz', True]