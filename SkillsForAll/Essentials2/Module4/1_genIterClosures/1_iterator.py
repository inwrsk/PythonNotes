#interation on obj
class oneToN:
    def __init__(self,e,s=1):
        print('init')
        self.start=s
        self.end=e
    def __iter__(self):
        print('iter')
        self.start=100
        self.end=102
        return self
    def __next__(self):
        print('next')
        if self.start>self.end:
            raise StopIteration
        else:
            self.start+=1
            return self.start-1
oneToNObj=oneToN(5)
#when for is initiated then
#iter is called it gives which object should be iterated upon
#and it iterates on the object(by calling next method) till iteration stops
for i in oneToNObj:
    print('for')
    print(i)
'''
init

iter

next
for
100

next
for
101

next
for
102

next
'''