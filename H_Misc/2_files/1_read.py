#rt or r for text files rb for bin files
stream=open(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module4\2_files\textfile',mode='r',encoding='UTF-8')
x=stream.read()
print(x)#first text
# stream.write('anwar')#UnsupportedOperation: not writable
x=stream.read()
print(x)#
#second read will not work as the pointer reached the end of file
stream.seek(1)#pointer will reach to nth position
print(stream.read())#first text