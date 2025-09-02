import firstfile
# __name__from_firstfile: firstfile
# __name__=='firstfile'from_firstfile
'''
when you run a file directly, its __name__ variable is set to __main__
when importing a module the execution of importing statement will be done
and there the __name__ is set to that module name in its execution
'''
print('from_secondfile:',__name__)
#from_secondfile: __main__