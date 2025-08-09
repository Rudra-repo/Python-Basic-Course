## LISTS IN PYTHON :-

# A built-in data type that stores set of values
# It can store elements of different types (integer, float, string,etc.)

# marks = [87,64,33,95,76]   #marks[0],marks[1]...

# student = ["Karan", 85,"Delhi"]  #student[0], student[1]..

# student[0] = "Arjun"     # allowed in python       ### Strings are immutable in python whereas lists are mutable (We can change the value in lists.)

# len(student)          # returns length 


marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(len(marks))
 

str = "hello" 
print(str[0])           # str[0] = "Y" [this value can't be assigned in str as we can't change value in a str at specific index in original statement]

# WHEREAS, in list we can change the value at specific index.

student = ["Karan", 95.4, "Delhi"]
print(student[0])
student[0] = "Arjun"
print(student)