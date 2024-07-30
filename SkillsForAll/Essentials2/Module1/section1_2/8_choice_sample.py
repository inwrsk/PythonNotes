from random import choice,sample

lst=[2,3,4,5]

print(choice(lst))#prints random element from the lst

print(sample(lst,3))#collect 3 random element from the lst
print(sample(lst,5))#ValueError:5 greater than the lst length we can do upto the lst length