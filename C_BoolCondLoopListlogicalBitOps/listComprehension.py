# List comprehension offers a shorter syntax for creating a new list based on the values of an existing list.

# --- Basic Example --- : The traditional way
squares_trad = []
for x in range(5):
    squares_trad.append(x**2)
print("Traditional way:", squares_trad)
# Traditional way: [0, 1, 4, 9, 16]

# The list comprehension way:
squares_comp = [x**2 for x in range(5)]
print("List comprehension:", squares_comp)
# List comprehension: [0, 1, 4, 9, 16]

#--- Example with multiple conditions and loops ---
# Create a list of numbers which are common in two lists (l1 and l2) AND are divisible by 6
l1 = [1, 2, 3, 4, 5, 6, 7, 12, 15, 21, 20, 96]
l2 = [12, 24, 96, 72]
# The multiple 'if' conditions can be combined with 'and' or by writing along side
common_and_div_by_6 = [i for i in l1 for j in l2 if i == j if  i % 6 == 0]
print("Divisible by 6 and common in both lists:", common_and_div_by_6)
# Divisible by 6 and common in both lists: [12, 96]

# --- Example with if-else ---
# An 'if-else' statement comes BEFORE the 'for' loop. It's used to change the output value.
# Add element's square if it's even, otherwise add the element itself.
l1 = [1, 2, 3, 4]
lst = [i**2 if i % 2 == 0 else i for i in l1]
print("Square if even, else the number itself:", lst)
# Square if even, else the number itself: [1, 4, 3, 16]

# --- (generating 2D lists) --- : Create a list of character lists from a list of words.
l1 = ["Anwar", "Shaik", "Siva sai"]
# The outer loop iterates through the words, the inner one through the characters of each word.
lst = [[char for char in word] for word in l1]
print("List of character lists:", lst)
# List of character lists: [['A', 'n', 'w', 'a', 'r'], ['S', 'h', 'a', 'i', 'k'], ['S', 'i', 'v', 'a', ' ', 's', 'a', 'i']]
