# del Keyword :-

# Used to delete object properties or object itself.

# del s1.name
# del s1

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rudra")

del s1.name         # Student name attribute has been deleted hence it's showing error when we try to print 's1.name'.

# PRIVATE(Like) ATTRIBUTES & METHODS :-

# Conceptual Implementations in Python:
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")

print(acc1.acc_no)
# print(acc1.__acc_pass)      #here we can't access the password as it's private
print(acc1.reset_pass())


class Person:
    __name = "annonymous"

    def __hello(self):
        print("hello person")           # these all cases are same as we use'__' to make it private so they have no attribute to print. Hence, giving error.

    def welcome(self):
        self.__hello()
p1 = Person()
# print(p1.__hello)

print(p1.welcome())

# INHERITANCE :-

# When one class (child/derived) derives the properties & methods of another class(parent/base).

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())
print(car1.color)

# INHERITANCE :-

# Types :

# Single Inheritance ( Example is already above.)
# Multi-level Inheritance
# Multiple Inheritance

#  This is an example of Multi-level Inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

# This is an example for Multiple Inheritance 

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

# SUPER METHOD :-

# super() method is used to access methods of the parent class.

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)

# Class Method :-

# A classs method is bound to the class & receives the class as an implicit first argument.

# Note:- Static method can't access or modify class state & generally for utility

class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name                    # It's basically changing the name of objects but not the name of class. So, we need to try out different indirect methods.

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name          # Here, we can change Person.name instead of self.name as self.name creates a different object and that changes only object name not the class name.

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)


class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "Rahul"      # Here, basically we are accessing class attribute using 'self.__class__' then we are changing name of class attribute and obj attr.

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

class Person:
    name = "anonymous"

    # def changeName(obj, name):
    #     self__class__.name = name

    @classmethod                            # This is the class methos, this directly changes the attribute in the class
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

# static methods [Does not change or access the attributes of both class and obj]
# class methods [class as a first implicit]
# instance methods[self]

# PROPERTY :-

# We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"           # Percentage

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"       # There's no problem with this method but to make it simple we use property decorators.

stu1 = Student(95,94,72)


stu1.phy = 89
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
        
stu1 = Student(95,94,72)

stu1.phy = 67
print(stu1.percentage)

# POLYMORPHISM : Operator Overloading :-
# When the same operator is allowed to have different meaning according to the context.

print(1+2)  #3
print(type(1))

print("Rudra"+" "+"Pratap")    # Concatenation
print(type("Rudra"))

print([1,2,3]+[4,5,6])      # merge
print(type([1,2,3]))

# this is operator overloading.

# Operators & Dunder functions(double underscore functions):-

# a + b     # additon                           a.__add__(b)
# a - b     # subtraction                       a.__sub__(b)
# a * b     # multiplication                    a.__mul__(b)
# a / b     # division                          a.__truediv__(b)
# a % b     # finding remainder                 a.__mod__(b)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2      # Here we can't directly use 'num1 + num2' to get the desired result as we haven't define the logic.
num3.showNumber()

num3 = num1 - num2
num3.showNumber()

