stream=open(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module4\2_files\textfile',mode='w+')
#all the previous data wipedout
#can perform read and write operations
print(stream.read())#
stream.write('stream write')
stream.seek(0)
print(stream.read())#stream write
stream.write('\nstream write2')
stream.seek(0)
print(stream.read())
'''
stream write
stream write2
'''