x=open('3_text')
print(x.readlines(15))#['first line\n', 'This is second line\n']#the pointer ends in second line
print(x.readlines(10))#['third line\n']#starts in 3rd line and end in itself
print(x.readlines())#['fourth line\n', 'this is fifth line']#from the pointer to end