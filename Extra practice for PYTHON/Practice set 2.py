# QUE: WAP to add two numbers.

a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))

sum = print(a+b)

# QUE: WAP to find the remainder when a number is divided by Z.

Y = int(input("Enter the no.: "))
Z = int(input("Enter the no.: "))

Remainder = Y%Z
if(Z < 0):
    print(-Z + Remainder)
else:
    print(Remainder)

# QUE: Check the type of variable assigned using input () function

a = input("Enter the val of a: ")
print(type(a))                      # Type of input is always str.

# QUE: Use comparison operator to find out whether a given variable a is greater than 'b' or not. Take a = 34 and b= 80

a = 34
b = 80
if(a>b):
    print("a is greater than 'b'.")
else:
    print("a not greater than 'b'.")

# QUE: WAP to find an avg of two no. entered by the user.

num_1 = int(input("Enter num_1 : "))
num_2 = int(input("Enter num_2 : "))

avg = (num_1+num_2)/2
print(avg)

# QUE: WAP to calculate the square of a number entered by the user.

num = int(input("Enter the no.: "))

sq_num = (num**2)
print("The square of the", num ,"is =", sq_num)