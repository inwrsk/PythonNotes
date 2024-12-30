for i in BaseException.__subclasses__():
    print(i)
'''
<class 'Exception'>
<class 'GeneratorExit'>
<class 'SystemExit'>
<class 'KeyboardInterrupt'>
'''
print(type(BaseException.__subclasses__()))#<class 'list'>