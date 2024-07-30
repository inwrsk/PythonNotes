def scope_test():
    x = 123
x=9
scope_test()
print(x)#9
#the function unable to change the variable value it is with in the func
#by using global we can do it
def scope_test2():
    global y
    print(y)#10
    y = 123
y=10
scope_test2()
print(y)#123

