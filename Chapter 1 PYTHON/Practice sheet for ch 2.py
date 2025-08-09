# QUE: Write a program to input to 2 numbers & print their sum.

a = int(input("a: "))
b = int(input("b: "))               # We can also add two decimal number just change datatype, it will be float via type casting.

sum = a+b
print("Sum:", sum)

# QUE: WAP to input side of a square & print its area.

side = float(input("side: "))

area = side*side
print("Area:", area)


# QUE: WAP to input 2 floating point numbers & print their avg.

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

avg = (num1+num2)/2
print("Average =", avg)


# QUE: WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.

a = int(input("a ="))
b = int(input("b ="))

if(a >= b):
    print(True)
else:
    print(False)
