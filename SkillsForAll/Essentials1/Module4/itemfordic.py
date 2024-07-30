dic={ 'key2':'value2',
    'key3':'value3'
}
dic2={  'key2':'value2',
}
#below i confused that what is i and i forgot to see that for is iterating on tuple
for i in (dic,dic2):
    print(type(i))
    print(i)
'''
<class 'dict'>
{'key2': 'value2', 'key3': 'value3'}
<class 'dict'>
{'key2': 'value2'}
'''