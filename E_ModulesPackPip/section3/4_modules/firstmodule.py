#!/usr/bin/env python3 
#For Unix-like OSs above line instructs the OS how to exec the contents of the file
""" module.py - an example of a Python module """
#this is doc-string => briefly explains about the module
__counter = 0

def sumlist(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum

def prodlist(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod

if __name__ == "__main__":
  print("I can do some tests for you")#I can do some tests for you
  my_list = [i+1 for i in range(5)]
  print(sumlist(my_list) == 15)#True
  print(prodlist(my_list) == 120)#True
  print(prodlist(my_list) == 120)#True
print('__counter:',__counter)#__counter: 3