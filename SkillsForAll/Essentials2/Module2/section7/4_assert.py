import math
try:
    x=-.9
    expression=x>=0.0
    assert expression#activates if none, 0 ,False expressions are passed
    print(math.sqrt(x))
except Exception as e:
    print(type(e))#<class 'AssertionError'>
try:
    x=9
    expression=x>=0.0
    assert expression
    print(math.sqrt(x))#3.0
except Exception as e:
    print(type(e))