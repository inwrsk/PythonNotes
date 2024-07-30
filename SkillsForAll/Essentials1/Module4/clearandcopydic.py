dic={ 'key1':'value1',
      'key4':{
        "key4.1":'value4.1',
        'key4.2':'value4.2'
    }
}
dic2=dic
print(dic is dic2)#True #both are pointing to the same dict
dic2=dic.copy()
print(dic2)#{'key1': 'value1', 'key4': {'key4.1': 'value4.1', 'key4.2': 'value4.2'}}
print(dic is dic2)#False #dic2 and dic are different
dic2={ 'key1':'value1',
      'key4':{
        "key4.1":'value4.1',
        'key4.2':'value4.2'
     }
}
print(dic is dic2)#False #dictionary is mutable so they are two different dic's
dic3=dic.clear()
print(dic)#{}
print(dic3)#None which is returned by the <class None>
print(dic2)#{'key1': 'value1', 'key4': {'key4.1': 'value4.1', 'key4.2': 'value4.2'}}
print(type(dic2.clear()))#<class 'NoneType'>
print(dic2)#{}