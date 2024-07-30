print(SyntaxError)#<class 'SyntaxError'>
if (1,1000>1000):
    print('yes')#yes
#here (1,1000>1000) is a tuple of 1,False so yes is printed
if 1,12>12:print('no')#here it is syntax error
if SyntaxError:#if something-> executes
    print('syntax_error')#syntax_error