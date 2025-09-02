class first:
    pass
class second(first):
    pass
class third (second):
    pass
#(subclass,superclass)#true
print(issubclass(first,first))#True

print(issubclass(second,first))#True
print(issubclass(third,first))#True
print(issubclass(third,second))#True

print(issubclass(first,second))#False

print(first.__subclasses__())#[<class '__main__.second'>]