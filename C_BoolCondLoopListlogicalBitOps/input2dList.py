#taking input of 2d lists using listcomprehension.
rows = input("Enter number of rows in 2d list : ")
lst = [[int(num) for num in input().split()] for i in range(int(rows))]
print("the matrix is : ", lst)
