# QUE: WAP to check if a number entered by the user is odd or even.

A = int(input("A: "))

if(A%2 == 0):
    print("EVEN")
else:
    print("ODD")

print("End of code")


# QUE: WAP to find the greatest of 3 numbers entered by the user.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest")
else:
    print("c is greatest")

print("End of code")


# QUE: WAP to check if a number is a multiple of 7 or not.

a = int(input("a: "))

if(a%7 == 0):
    print("a is a multiple of 7")
else:
    print("a is not multiple of 7")

print("End of code")