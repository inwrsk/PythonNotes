class first:
    var=1
class second(first):
    var=3
class third(second,first):#multipleinheritance
    pass
obj=third()
print(obj.var)#3
# class fourth(first,second):pass# error
class fourth (second):pass
obj=fourth()
print(obj.var)#3
#the order of inheritance is current class then the super class just above et.. to the root