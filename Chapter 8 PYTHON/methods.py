# METHODS :-
# Methods are functions that belong to objects.

# Class is of two types:-
# 1. data (attr)       [Basically, it tells about the properties that you are having. like, it tells about color, brand and so on features]
# 2. Methods           [While, it tells about functions of the particular object ,like how a car starts and so on. ]

# creating class

# class Student:
#     def __init__(self,fullname):
#         self.name = fullname

#         def hello(self):
#             print("hello",self.name)

# creating object:
# s1 = Student("Rudra")
# s1.hello()

class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks
    
s1 = Student("Rudra", 97)

s1.welcome()
print(s1.get_marks())

# LET'S PRACTICE :-

# QUE: Create student classs that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "\nYour avg score is: ", sum/3)

s1 = Student("Rudra", [98,94,93])
s1.get_avg()

s1.name = "Pratap"
s1.get_avg()

# STATIC METHODS :-

# Methods that don't use the self parameter (work at class level)

# class Student:
    # @staticmethod         # decorator
    # def college():
        # print("ABC College")
    
# Decorators :- Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "\nYour avg score is: ", sum/3)

s1 = Student("Rudra", [98,94,93])
s1.get_avg()

s1.name = "Pratap"
s1.get_avg()
s1.hello()

# IMPORTANT :-

# Abstraction :- Hiding the implementation detials of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()

# Encapsulation :- Wrapping data and functions into a single unit (object).

# LET'S PRACTICE :-

# QUE: Create Account class with 2 attributes - balance & account no.
#      Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

 # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

# credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

