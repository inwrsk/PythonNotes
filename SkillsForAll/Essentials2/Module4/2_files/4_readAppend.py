#r+ or r+t for text files and r+b for bin files
stream=open(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module4\2_files\textfile',mode='r+')
#willnot wipe the previous data
#similar to append and read
print(stream.read())
'''
first text
this is anwar
'''
stream.write('\nread and update')
stream.seek(0)#for moving pointer to start
print(stream.read())
'''
first text
this is anwar
read and update
'''