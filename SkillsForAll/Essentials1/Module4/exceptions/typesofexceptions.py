try:
    print('start of try block')
    #print([1,2,3][23])#-> Index Error(list index out of range)
    #print(0/0)#->ZeroDivisionError(division by zero)
    #y=float('anwar')#-> ValueError(could not convert string to float: 'anwar')
    #'anwar'+43#Type Error(can only concatenate str (not "int") to str)
    #print([1,2,3].depend(4))#-> attribute error('list' object has no attribute 'depend')
    #print(x)#->NameError(name 'x' is not defined)
    #exec('print)();')#-> when you enter wrong code SyntaxError
except IndexError as e:
    print('index error->',e)
except ZeroDivisionError as e:
    print('zero division error->',e)
except ValueError as e:
    print('value error->',e)
except TypeError as e:
    print('type error->',e)
except AttributeError as e:
    print('attribute error->',e)
except NameError as e:
    print('this is name error->',e)
except SyntaxError as e:
    print('syntax error->',e) 
except BaseException as e:
    print(e,type(e))