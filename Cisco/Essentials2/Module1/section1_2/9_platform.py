from platform import *
#access the underlying platform's hardware, os, and interpreter version
print(system())#Windows
print(version())#10.0.22631

print(platform())#Windows-10-10.0.22631-SP0
print(platform(aliased=0,terse=0))#Windows-10-10.0.22631-SP0

print(platform(1))#Windows-10-10.0.22631-SP0
print(platform(0,1))#Windows-10

print(platform(aliased=1,terse=10))#Windows-10
'''
aliased → cause the function to present the underlying layer names ;
terse → convince the function to present a briefer form of the result (if possible)
'''

#for other platforms eg:
'''
Raspberry PI2 + Raspbian Linux (32 bit)
Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
'''
print(machine())#AMD64
print(processor())#Intel64 Family 6 Model 140 Stepping 1, GenuineIntel

print(python_implementation())#CPython
print(python_version())#3.10.11