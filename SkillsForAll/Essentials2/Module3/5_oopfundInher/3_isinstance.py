class first:
    pass
class second(first):
    pass
class third (second):
    pass
firstObj=first()
secondObj=second()
thirdObj=third()
print(isinstance(firstObj,first))#True

print(isinstance(secondObj,first))#True
print(isinstance(thirdObj,first))#True
print(isinstance(thirdObj,second))#True

print(isinstance(firstObj,second))#False
