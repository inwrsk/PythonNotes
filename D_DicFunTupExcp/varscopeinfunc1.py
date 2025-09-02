#observe the order and scope carefully
def func(list1):
    #here list1 is pointer pointing to ['anwar'] when the line below is executed list1 is assigned to another list which is function scope    
    list1=['anwarshaik']
    list3=list1
    print('list1',list1)#['anwarshaik']
    del list3#deleting the pointer
    print('list1',list1)#['anwarshaik']
    print('list2',list2)#['anwar']
    list1=['shaik']
list2=['anwar']
func(list2)
print(list2)#['anwar']
