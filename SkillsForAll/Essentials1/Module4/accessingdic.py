dic={ 
      'key2':'val2',
      'key1':'val1',
         '3':'val3',
      'key4':{
                "key4.1":'val4.1',
                     4.2:'val4.2'
             }
    }
print(dic)#{'key2': 'val2', 'key1': 'val1', '3': 'val3', 'key4': {'key4.1': 'val4.1', 4.2: 'val4.2'}}
print(dic['key2'])#val2
print(dic['key4']['key4.1'])#val4.1
print(dic.keys())#dict_keys(['key2', 'key1', '3', 'key4'])
print(type(dic.keys()))#<class 'dict_keys'>
print(sorted(dic.keys()))#['3', 'key1', 'key2', 'key4']
print(type(sorted(dic.keys())))#<class 'list'>
print(dic.values())#dict_values(['val2', 'val1', 'val3', {'key4.1': 'val4.1', 4.2: 'val4.2'}])
print(type(dic.values()))#<class 'dict_values'>
print(sorted(dic['key4'].values()),type(sorted(dic['key4'].values())))#['val4.1', 'val4.2'] <class 'list'>