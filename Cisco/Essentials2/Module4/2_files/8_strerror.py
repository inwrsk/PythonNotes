from os import strerror
try:
    s=open('sdfs')
except BaseException as e:
    print(strerror(e.errno))#No such file or directory
#gives the explanation of a error
#it again raises unknownError if wrong errno was given
try:
    1/0
except Exception as e:
    print(strerror(2456723))#unknownError