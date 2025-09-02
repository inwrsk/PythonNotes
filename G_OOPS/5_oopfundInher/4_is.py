class SampleClass:
    def __init__(self, val):
        self.val = val

object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)#False
print(object_2 is object_3)#False
print(object_3 is object_1)#True
print(object_1.val, object_2.val, object_3.val)#1 2 1

string_1 = "a "
print(id(string_1))#2818927356272
string_2 = "a b"
print(id(string_2))#2818927356016
string_1 += "b"
print(id(string_1))#2818927369840
string_3='a b'
print(id(string_3))#2818927356016

print(string_1 is string_2)#False    
print(string_3 is string_2)#True