from os import strerror#takes int values
try:
    stream=open('1_text')
    print(stream.readline(),end='')#Anwar Shaik #firstline
    print(stream.read(4))#is a #some part of firstline
    print(stream.readline())# good boy. #pointer to the end of line
except IOError as e:
    print(strerror(e.errno),e.errno)#error discription and a integer value