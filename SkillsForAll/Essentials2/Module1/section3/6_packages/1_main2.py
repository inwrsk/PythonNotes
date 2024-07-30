from sys import path
path.append(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module1\section3\packages')

import extra
#print(extra.FunT()) #wecan't directly do that
print(extra.good.best.tau.FunT())
print(extra.ugly.psi.FunP())

#Python doesn't automatically import submodules
#if you want to access the values directly with the package name then
#import the modules or what ever in the __init__.py of packages
#and also add their paths in the main package __init__.py file or individual in init files of individual folders
'''
extra package is runnning
best package is running
good package is running
ugly package is running
Tau
Psi
'''