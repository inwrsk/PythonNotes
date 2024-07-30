print('__name__from_firstfile:',__name__)
#__name__from_firstfile: __main__
if __name__=='__main__':
    print("__name__=='__main__'from_firstfile")
    #__name__=='__main__'from_firstfile
if __name__=='firstfile': 
    print("__name__=='firstfile'from_firstfile")
if __name__=='secondfile':
    print("__name__=='secondfile'from_firstfile")
if __name__=='thirdfile':
    print("__name__=='thirdfile'from_firstfile")
if __name__ not in ['__main__','secondfile','firstfile']:
    print("__name__ not in ['__main__','secondfile','firstfile']")