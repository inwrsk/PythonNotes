#BaseException ← Exception ← ArithmeticError
#eg:it contains errors like zerodivision

#BaseException ← Exception ← AssertionError
#raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string

#BaseException
#it is parent of all

#BaseException ← Exception ← LookupError ← IndexError
#[1,2,3,4][5]

# BaseException ← KeyboardInterrupt
#when ctrl+c is pressed
def keyboard():
    try:
        input()#enter cntrl c
    except KeyboardInterrupt:
        print('you interrupted')
#keyboard()#you interrupted

# BaseException ← Exception ← LookupError
#caused by errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)
def lookup():
    try:
        dic={
            'key':'value'
        }
        print(dic['asdf'])
    except LookupError as e:
        print(type(e))
#lookup() #<class 'KeyError'>

#BaseException ← Exception ← MemoryError
#raised when an operation cannot be completed due to a lack of free memory.
def memError():
    string='sfs'
    try:
        while True:
            string+=string*10000000
    except MemoryError:
        print('Memory Error')
#memError() #Memory Error

#BaseException ← Exception ← ArithmeticError ← OverflowError
#raised when an operation produces a number too big to be  stored
import math
def Overflow():
    try:
        #print(2345e234*234534534.535e234234)#inf
        #when using arithmetic operations b/w integers or 
        #operations b/w two scietific notation float numbers
        #error won't occur
        #only when floating point numbers reach their max limit 
        #that too both should not be in scientific notation
        print(2345e234*234534534.535*10**234234)#error
    except OverflowError:
        print('error')
Overflow() 

#BaseException ← Exception ← StandardError ← ImportError
#when an import operation fails
#eg:import asdfsfdsg