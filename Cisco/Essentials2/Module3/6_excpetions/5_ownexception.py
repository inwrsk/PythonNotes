class ownExeception(ZeroDivisionError):
    pass
print(Exception.__subclasscheck__(ownExeception))#True
#as ownException in zeroDivsionError and zero in Exception
try:
    raise ownExeception
except ZeroDivisionError:
    print('zerodivisionerror')#zerodivisionerror


class ownException2():
    pass
print(Exception.__subclasscheck__(ownException2))#False

try:
    raise ownException2
except ZeroDivisionError:
    print('Exception')
except:
    print('not in Exception')#not in Exception #TypeError

try:
    raise ownException2
#except ownException2:
#TypeError: catching classes that do not inherit from BaseException is not allowed
    print('ownException2')
except:
    print('default')#default