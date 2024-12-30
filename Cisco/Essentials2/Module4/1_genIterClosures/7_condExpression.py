lst=[1]
lst.append('if' if True else 'else')
print(lst)#[1, 'if']

evenList=['X' if x%2==1 else x for x in range(6)]
print(evenList)#[0, 'X', 2, 'X', 4, 'X']