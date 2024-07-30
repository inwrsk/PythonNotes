class className():
    def  __init__(self,a,c,b=1):#a=1,b not permitable you can do b,a=1
        self.value1=a
        self.value2=b
        self.__list=['sample','list']
    def func(self):
        print('sample func')
#Obj4=className(1)# c not assigned
Obj5=className('1','3')#we can pass 3 arguments also
print(Obj5.__dict__)#{'value1': '1', 'value2': 1, '_className__list': ['sample', 'list']}
#__dict__ is a variable contains names, values of the objects
