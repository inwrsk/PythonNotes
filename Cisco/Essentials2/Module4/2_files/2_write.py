#wt or w for text files wb for bin
stream=open(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module4\2_files\pythonfile.py',mode='w')#can create new file
#wipes out the previous data
x='print("hello Python")'
stream.write(x)
# y=stream.read()#UnsupportedOperation: not readable
stream.close()