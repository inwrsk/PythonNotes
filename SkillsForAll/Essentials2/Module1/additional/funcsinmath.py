from math import *

#radians and degrees will modify the magnitude but both are treated as radians only
print(type(degrees(pi)))#<class 'float'>
print(type(radians(degrees(pi))))#<class 'float'>

print(sin(pi/2),cos(pi/2),tan(radians(180)),tan(degrees(pi)),sep=' , ')#so tan(180) here is not near to 0
#1.0 , 6.123233995736766e-17 , -1.2246467991473532e-16 , 1.3386902103511544

#values are not accurate bcz we can't get exact value of pi
print(cos(22/7))#-0.999999200533553

print(e,exp(1))#2.718281828459045 2.718281828459045
print(exp(2),e**2)#7.38905609893065 7.3890560989306495

print(log(e),log2(4),log10(100))#1.0 2.0 2.0

print(ceil(1.5),ceil(-1.5))#2 -1

print(floor(1.5),floor(-1.5))#1 -2

print(trunc(1.4),trunc(1.6))#1 1
print(trunc(-1.5))#-1

print(factorial(5))#120

print(pow(3,2))#9.0