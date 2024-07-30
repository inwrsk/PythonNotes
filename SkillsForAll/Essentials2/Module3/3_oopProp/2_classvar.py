class ExampleClass:
    counter = 0#same if you make it private __counter
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

example_object_1 = ExampleClass()
print(ExampleClass.counter)#1
example_object_2 = ExampleClass(2)

print(example_object_1.__dict__, example_object_1.counter)#{'_ExampleClass__first': 1} 2
print(example_object_2.__dict__, example_object_2.counter)#{'_ExampleClass__first': 2} 2
example_object_1.counter=10#new object variable created 
print(example_object_1.__dict__, example_object_1.counter)#{'_ExampleClass__first': 1, 'counter': 10} 10
print(example_object_2.__dict__, example_object_2.counter)#{'_ExampleClass__first': 2} 2
ExampleClass()
print(example_object_1.__dict__, example_object_1.counter)#{'_ExampleClass__first': 1, 'counter': 10} 10
print(example_object_2.__dict__, example_object_2.counter)#{'_ExampleClass__first': 2,} 3
#once the object var is created it will not change to class var again