def fun1(n):
    for i in range(n):
        yield i
print(1 in fun1(3), 2.0 in fun1(3),3 in fun1(3))#True True False