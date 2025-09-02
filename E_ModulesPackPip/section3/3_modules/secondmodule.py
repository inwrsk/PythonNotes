#to say that we can change the values of module but temporary
import firstmodule
# first_module: __name__= firstmodule
# 0
print('secondmodule: __name__',__name__)
print(firstmodule.__counter)
firstmodule.__counter='counter'
print(firstmodule.__counter)