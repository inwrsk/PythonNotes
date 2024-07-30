def func(list1):
    list1=['anwarshaik']
    print('list1',list1)#['anwarshaik'] will not print because of single line nature of function
    print('list2',list2)#list2 referenced before assignment
    list2=[1,2,3]
    #here you might think first list2 is global and second is local but it's not the way it works 
    #entire function is treated as single line so it will consider all the lines as single line simultaneously and 
    #the reason for error
list2=['anwar']
func(list2)
print(list2)#['anwar'] will not be executed