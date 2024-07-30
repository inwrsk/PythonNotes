#internally
def func(num):
    try:
        print(1/num)
    except BaseException as e:
        print(type(e))
func(0)#<class 'ZeroDivisionError'>
func('asfdj')#<class 'TypeError'>
#externally
def func(num):
    print(1/num)
try:
    func(0)
except (BaseException,ZeroDivisionError) as e:
    print(type(e))#<class 'ZeroDivisionError'>