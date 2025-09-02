class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def increaseIntI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)#obj.name
            if isinstance(val, int):#type(val)==int
                setattr(obj, name, val + 1)#obj.name=val+1

print(obj.__dict__)#{'a': 1, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
increaseIntI(obj)#increase varible value by 1 whose name starts with i
print(obj.__dict__)#{'a': 1, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}