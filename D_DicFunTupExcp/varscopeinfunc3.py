#observe the order and scope carefully
def func(list1):
    list1=['shaik']
    print('list1',list1)#['shaik']
    print('list2',list2)#['anwar']
    #here list2 is accessed globally before it conclude like this it will first check whether any list2 is
    #declared with in the function whether top of it or bottom of it because function acts as a single line
list2=['anwar']
func(list2)
print(list2)#['anwar']