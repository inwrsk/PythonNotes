try:
    print('before error')#before error
    print(0/0)
    #the code afte error is not going to be executed
    print('after error')
except:
    print('unexpected error')#unexpected error
print('normal ending')#normal ending