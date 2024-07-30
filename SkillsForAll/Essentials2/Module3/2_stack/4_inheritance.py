class superClass:
    def __init__(self):#self denotes a object
        print('constructor of superClass')
        self.__stackList=[]
        self.var='Normal Varible'
    def push(self,val):
        self.__stackList.append(val)
        print(self.__stackList)
    def pop(self):
        val=self.__stackList[-1]
        del self.__stackList[-1]
        return val
class empty:
    pass
emptyObj=empty()
#we can add attributes to this object
def funcPrint():
    print('funcPrints')
emptyObj.func=funcPrint
emptyObj.func()#funcPrints
print(dir(emptyObj)[-1])#func

#superClass.push(emptyObj,'firstvalue')#'empty' object has no attribute '_superClass__stackList'
#we can use only the funcs of superClass which don't use obj init.
#but to achieve this we need to send this object to constructor it will add the req properties
superClass.__init__(emptyObj)#constructor of superClass
print(emptyObj.var)#Normal Varible
print(emptyObj._superClass__stackList)#[]
superClass.push(emptyObj,'firstvalue')#['firstvalue']

#what if we create a variable _superClass_stackList on our own?
newEmptyObj=empty()
newEmptyObj._superClass__stackList=[]
superClass.push(newEmptyObj,'1value')#['1value']
#so if we have all the necessary elements for the func of a class in our obj
#we can execute it i.e creating the object of our own

class emptySubClass(superClass):
    pass
#emptySubClass has all the attributes superClass even the constructor
emptySubClassObj=emptySubClass()#constructor of superClass
emptySubClassObj.push('anwar')#['anwar']
print(emptySubClassObj._superClass__stackList)#['anwar']
#so why _superClass ?because the __stackList is private it is accessed only with _IT"s_ class name
#remember any private attribute can be accessed with the class name containing it
#even in inheritance 

#if a subclass have some properties then 
#the object will get the properties and then the superclass properties too
#if the properties or attributes names are equal subclass's properties are give higher priority
#this is called overriding
class SubClass(superClass):
    def push(self,val):
        self._superClass__stackList.append(val*10)
        print(self._superClass__stackList)
SubClassObj=SubClass()#constructor of superClass
print(SubClassObj._superClass__stackList)#[]
print(SubClassObj.var)#Normal Variable
SubClassObj.push('k')#['kkkkkkkkkk'] #method of subClass
print(SubClassObj.pop())#kkkkkkkkkk #method of superClass

#what if we have our own constructor ?
#having own constructor mean having own values
class SubClass2(superClass):
    def __init__(self):
        self.__miniStackList=[]
        print('constructor of SubClass2')
SubClass2Obj=SubClass2()#constructor of SubClass2
#print(SubClass2Obj._superClass__stackList)#'SubClass2' object has no attribute '_superClass__stackList'
#print(SubClass2Obj.var)#'SubClass2' object has no attribute 'var'
print(SubClass2Obj._SubClass2__miniStackList)#[]
#what happenend ?
#as we created our own constructor it is prioritized more than superClass's Constructor
#and also we can access then methods of superClass push and pop but no use as we don't have the
#__stackList on which the operations are done
#but there is a method-> create a stackList on your own
#SubClass2Obj.push('Test')#'SubClass2' object has no attribute '_superClass__stackList'
#as we said
SubClass2Obj._superClass__stackList=[]
SubClass2Obj.push('Test')#['Test']
#now we can use the other functions too

#is there any process to have the values of the Superclass als0?
#yes call it's constructor
#in outside after object created or in the constructor of subclass itself
class SubClass3(superClass):
    def __init__(self):
        superClass.__init__(self)
        self.__miniStackList=[]
        print('constructor of SubClass2')
subClass3Obj=SubClass3()
# constructor of superClass
# constructor of SubClass2

#what if we have some common variables
class SubClass4(superClass):
    def __init__(self):
        self.var='SubClass4 Variable'
        print(self.var)#SubClass4 Variable
        superClass.__init__(self)#constructor of superClass
        print(self.var)#Normal Variable
        superClass.__init__(self)#constructor of superClass
        self.__miniStackList=[]
        print('constructor of SubClass4')#constructor of subClass4
subClass4Obj=SubClass4()
print(subClass4Obj.var)#Normal Varible
#it means the last value is updated