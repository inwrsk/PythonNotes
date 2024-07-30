#by default the mode will be text
#to open nontext files we need bin mode
stream=open(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module4\2_files\2_python.jpg',mode='r+b')
x=stream.read()
print(x)
stream2=open(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module4\2_files\1_python.jpg',mode='wb')#created new imagefile
stream2.write(x)
stream.seek(0)
stream.write(b'binary\x11')#currepting the image file(changing)
print(stream.read())