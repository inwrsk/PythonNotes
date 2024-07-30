#if the module is not in current dir then add to path and use
import sys,math
for p in sys.path:
    print(p)
# c:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module1\section3.py\5_modulesPath.py
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\python310.zip   
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\DLLs
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib
# C:\Users\Anwar Shaik\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0      
# C:\Users\Anwar Shaik\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages
# ackages\Python310\site-packages\win32
# C:\Users\Anwar Shaik\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\win32\lib
# C:\Users\Anwar Shaik\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\Pythonwin
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\site-packages

'''
this consists paths that are used to search the modules we want to import 
'''

print(math.e)#2.718281828459045

'''
the main math module was imported because of highest preference
if the highest preference folders not available then local folder will be searched
'''

#import firstmodule => shoots error because the sys.path donot contain the folder consisting this module
#to access it add the directory to the sys.path
sys.path.append(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module1\section3.py\4_modules')
print(sys.path[-1])
#C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module1\section3.py\4_modules
exec('import secondmodule')
#__counter: 0
#10
#1