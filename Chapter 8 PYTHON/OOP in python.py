# OOP in PYTHON :- 

# TO map with real world scenarios, we started using objects in code.
# this is called object oriented programming.

a = 10
b = 20

sum = a+b           #Procedural programming , then we shifted to functional programming now we are learning object oriented programming.
print(a+b)

diff = a - b
print(diff)

# Class & Object in python:-

# Creating class
class Student:
    name = "Rudra Pratap"

# Creating object (instance)

s1 = Student()
print(s1.name)

# s2 = Student()
# print(s2.name)


class Car:
    colour = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.colour)
print(car1.brand)

# __init__ Function :-
# Constructor:-
# All classes have a function called __init__(), which is always executed when the class is being initiated.

# creating class
class Student:
    def __init__(self,fullname):                                      
        self.name = fullname

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# creating object
s1 = Student("Rudra")
print(s1.name)

# Parameterized constructors
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database...")

s1 = Student("rudra", 97)

print(s1.name,s1.marks)  # Rudra Pratap

s2 = Student("arjun", 88)
print(s2.name, s2.marks)

# Attributes -> The data or the variable that are stored is called attributes.

# default constructors
def __inti__(self):
    pass

# Class & Instance Attributes :-

# Class.atr
# obj.attr

class Student:
    college_name = "ABC College"
    name = "anonymous"      # class attr [ when we have both class attr and obj attr then prefrence is given to obj attr]

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database...")

s1 = Student("rudra", 97)

print(s1.name,s1.marks)  # Rudra Pratap

s2 = Student("arjun", 88)
print(s2.name, s2.marks)

print(Student.college_name)

