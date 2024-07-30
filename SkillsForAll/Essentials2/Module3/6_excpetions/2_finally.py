def reciprocal(n):
    try:
        n = 1 / n
    except :
        #exception is a class
        #when exception is raised the object will be created
        print("except")
    else:
        print("else")
    finally:
        print("finally")
    print('after finally')

reciprocal(2)
# else
# finally
# after finally
reciprocal(0)
# else
# finally
# after finally