# QUE: WAP to store seven fruits in a lists entered by the user.

fruits = []

f1 = input("Enter Fruit here: ")
fruits.append(f1)

f2 = input("Enter Fruit here: ")
fruits.append(f2)

f3 = input("Enter Fruit here: ")
fruits.append(f3)

f4 = input("Enter Fruit here: ")
fruits.append(f4)

f5 = input("Enter Fruit here: ")
fruits.append(f5)

f6 = input("Enter Fruit here: ")
fruits.append(f6)

f7 = input("Enter Fruit here: ")
fruits.append(f7)

print(fruits)

# QUE: WAP to accept fruits of 6 students and display them in a sorted manner.

marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)

f2 = int(input("Enter Marks here: "))
marks.append(f2)

f3 = int(input("Enter Marks here: "))
marks.append(f3)

f4 = int(input("Enter Marks here: "))
marks.append(f4)

f5 = int(input("Enter Marks here: "))
marks.append(f5)

f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()
print(marks)

# QUE: Check that tuple type cannot be changed in python.

tup = (56,67,56,45,34,45)

tup[3] = 34
print(tup)          # hence it will give error.

# QUE: WAP to count the no. of zeroes in the following tuple:

a = (7,0,8,0,0,9)

b = a.count(0)
print(b)

# QUE: WAP to sum a list with 4 numbers.

list = [34,54,67,2]

print(sum(list))

