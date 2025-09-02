def tryElse(n):
    try:
        1/n
    except:
        print('error')
    else:
        print('no error')
tryElse(0)#error
tryElse(4)#no error