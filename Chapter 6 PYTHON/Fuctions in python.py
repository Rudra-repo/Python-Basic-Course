# FUNCTIONS IN PYTHON :
#  Block of statements that perform a specific task.                # REPEAT/REDUNDANT

# def func_name(parameter1, parameter2..) :                 # input(parameter) --> function --> output 
        # some work
        # return val

# func_name( arg1, arg2..) # function call

def sum(a, b):
    s = a+b
    return s
print(sum(1,2))

a = 5
b = 10
sum = a+b
print(sum)



#  more lines of code

a = 2
b = 5
sum = a+b 
print(sum)


# more lines of code 

# then again sum of two no. ,
    #  here code is repeating so we can use functions here.


def calc_sum(a, b):
    sum = a+b
    print(sum)
    return sum 

calc_sum(34, 43)

# Function definition :-
def calc_sum(a,b):
    return a + b 

sum = calc_sum(1, 2)
print(sum)

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

def print_hello():
    print("hello")

output = print_hello()
print(output)      # None


# average of 3 numbers

def calc_avg(a, b, c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(1,2,3)
calc_avg(97,95,94)

# Functions in python are of two types :-

# 1. Built-in functions     [print(), len(), type(), range()]
# 2. User defined functions 

print("Rudra","pratap")     # sep = " "
print("Rudra", end=" ")
print("pratap")             # end = " " that print two line in single as end is with space

print("Rudra\nPratap")      # '\n' shows to end line start with next line.

def cal_prod(a, b=2):           # When we have to give default values then give it at last ex: (a=3,b) gives you error whereas (b,a=3) give actual result.
    print(a * b)
    return a*b

cal_prod(3)