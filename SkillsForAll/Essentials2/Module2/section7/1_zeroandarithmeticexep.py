#zeroDivisionError is spcl case in ArithmeticError
try:
    1/0
except ZeroDivisionError:
    print('zero')#zero
except ZeroDivisionError:
    print('zero2')
except ArithmeticError:
    print('Arithmetic')

print('first stop')#first stop

try:
    1/0
except ArithmeticError:
    print('Arithmetic')#Arithmetic
except ZeroDivisionError:
    print('zero')

print('secondStop')#secondStop
try:
    int(input())
    1/0
except (ArithmeticError,ValueError):
    print('error')#error
print('third stop')#third stop