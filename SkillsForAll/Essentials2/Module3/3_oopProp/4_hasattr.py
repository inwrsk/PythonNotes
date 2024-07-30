class hasAttrClass:
    counter=1
    def __init__(self,a):
        if a==1:
            self.p='p'
            hasAttrClass.counter+=1
        else:self.q='q'
    def func(self):
        print('self')
print(hasattr(hasAttrClass,'counter'),hasattr(hasAttrClass,'p'))#True False
obj=hasAttrClass(1)
print(hasattr(obj,'counter'),hasattr(obj,'p'),hasattr(obj,'q'))#True True False
print(hasattr(hasAttrClass,'counter'),hasattr(hasAttrClass,'p'))#True False
print(hasattr(obj,'func'),hasattr(hasAttrClass,'func'))#True True
print(obj.__dict__,hasAttrClass.__dict__)
'''
{'p': 'p'} 
{'__module__': '__main__', 'counter': 2, '__init__': <function hasAttrClass.__init__ at 0x000001E1F938B130>, 'func': <function hasAttrClass.func at 0x000001E1F938B1C0>, '__dict__': <attribute '__dict__' of 'hasAttrClass' objects>, '__weakref__': <attribute '__weakref__' of 'hasAttrClass' objects>, '__doc__': None}
'''