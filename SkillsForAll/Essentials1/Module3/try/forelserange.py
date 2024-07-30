for i in range(0,4,2):
    print(i)#0#2
    i*=100
else:print(i)#200
#else i will be the last i value inside the loop
print()
for i in range(0,8,2):
    if i==6:break
    print(i)#0#2#4
else:print(i*10)#else will not exec if loop breaks
print(i*100)#600