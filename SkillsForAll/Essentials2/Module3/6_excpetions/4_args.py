try:
    raise Exception
except Exception as e:
    print(e,type(e))# <class 'Exception'>
    print(e.args)#()

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, type(e))#('my', 'exception') <class 'Exception'>
    print(e.args)#('my', 'exception')