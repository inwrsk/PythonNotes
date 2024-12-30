lst=[i for i in range(5)]
gen=(i for i in range(5))
# print(len(gen))#'generator' has no len()
print(type(lst),type(gen))#<class 'list'> <class 'generator'>
print(list(gen))#[0, 1, 2, 3, 4]