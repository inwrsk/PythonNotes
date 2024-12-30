x=10
y=x
x=11
print(y)#10
#the above 4 lines to observe y only stores the value
list1=[1]
list2=list3=list1
#<--------------
#the above list 2,3 stores the address of the [1]
list1=[2]
#here [2] is a new list which list1 is pointing to
print(list2,list3)#[1] [1]
#still list2,3 pointig to [1]
list3[0]='anwar'#modifying the value inside [1] which is array but they still pointing to the same array
print(list2,list3)#['anwar'] ['anwar']