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
class sumUp(stack):
    def __init__(self):
        stack.__init__(self)
        self.__sum=0
    def push2(self,val):
        sumUp.push(self,val)#or stack.push both are same as we inherited the stack and have no overrides
        self.__sum+=val
    def pop2 (self):
        val=stack.pop(self)#sumUp.pop
        self.__sum-=val
        return val
    def getSum(self):
        return self.__sum
stack_obj=sumUp()
for i in range(5):
    stack_obj.push2(i)
    print(stack_obj.getSum(),end=' ')#0 1 3 6 10
print()
for i in range(5):
    print(stack_obj.pop2(),end=' ')#4 3 2 1 0