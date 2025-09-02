lists=[34,'3rf',234.234,'afdsf',False]
lists.insert(1,'this is in the second position')
print(lists)#[34, 'this is in the second position', '3rf', 234.234, 'afdsf', False]
lists.insert(-1,'this is in the second last position')
print(lists)#[34, 'this is in the second position', '3rf', 234.234, 'afdsf', 'this is in the second last position', False]