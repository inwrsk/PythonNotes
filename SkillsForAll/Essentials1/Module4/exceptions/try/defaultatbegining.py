try:
    #default except
    print()
except:
    print('they say default except should always at the end')
except ValueError:
    print("value error")
except ZeroDivisionError:
    print('cannot perform division with zero')
#this shoots error as default except should be at the bottom