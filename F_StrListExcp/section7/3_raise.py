try:
    raise ArithmeticError
except BaseException as e:
    print(type(e))#<class 'ArithmeticError'>
print('_______')
try:
    raise#by default it causes RuntimeError
except BaseException as e:
    print(type(e))#<class 'RuntimeError'>
print('_______')
def bad_fun():
    try:
        1/'anwar'
    except:
        print('error in func')
        raise#the error which it caught will be raised again
try:
    bad_fun()
except BaseException as e:
    print(type(e))