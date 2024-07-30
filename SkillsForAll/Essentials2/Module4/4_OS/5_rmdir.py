import os
os.chdir('second_direc')#['subdirec','second sub directory']
os.rmdir('second sub directory')#removes the directory (present in the current woking directory)
print(os.listdir())#['subdirec']