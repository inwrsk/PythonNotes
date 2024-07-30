class Hi:
    def __init__(self):#constructor (self denotes the objects which we create)
        print('Hi')
Hi_obj=Hi()#Hi
#constructor will implicitly invokes while creating obj

class stack:
    def __init__(self):
        self.__stack_list=[]
    def push(self,val):
        self.__stack_list.append(val)
    def pop(self):
        val=self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
stack_obj=stack()

#print(len(stack_obj.__stack_list))#can't access the variables with __(encapsulation)
print(stack_obj._stack__stack_list)#[]#we can access protected variables like this _classname+varname
stack_obj.push(3)#whenever a method invokes the obj is sent as first arg. i.e self
stack_obj.push(7)
print(stack_obj.pop())#7
print(stack_obj._stack__stack_list)#[3]