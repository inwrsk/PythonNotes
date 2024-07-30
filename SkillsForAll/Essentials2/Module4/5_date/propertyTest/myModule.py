class myClass:
    @property#by declaring like this we will get return value without invovation myClass().myFunc
    def myFunc(self):
        return 'myVal'
    #not declaring by @property is initialized by myClass().myFunc2()
    def myFunc2(self):
        return 'myVal2'