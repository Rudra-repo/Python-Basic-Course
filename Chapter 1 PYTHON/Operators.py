# Types of Operators :-
# Arithmetic Operators (+,-,*,/,//,%,**)
# Relational/Comparison opertors (==,!=,<,>,>=,<=)
# Assignment operators (=,-=,+=,/=,//=,*=,%=,**=)
# Logical operators (not,and,or)        [Operation Precidence/order : not > and > or]
# Membership operators (in,not in)
# Bitwise operators (&,|,^)


# Arithmetic Operators :-

a = 4
b = 3

print(a+b)              # To add the numbers
print(a-b)              # To subtract the numbers
print(a*b)              # To multiply the numbers
print(a/b)              # To divide the numbers
print(a//b)             # To Find the GIF (greatest integer function)
print(a**b)             # To Find the a^b of numbers
print(a%b)              # To find the remainder of numbers (detailed explanation, in punctuators)

## Similar way all the operators works wheather Relational operators or as Assignment operators.

A,B=2,3
C=4                      # Numeric values can operates with all the arithmetic operators.
print(A+B*C)

A,B=10,5.0
C=A*B                    # Arithmetic expression with integers and float will result in float.
print(C)

A,B=1,2
C=A/B                   # Result of division operators with two integers will be float.
print(C)


A,B=1.5,3
C=A//B                  # Integer division with float and int give int displayed as float.
print(C,A/B)            # Inter with '//' sign gives Gif (Greatest integer function) value.


A,B=-5,2 # ("%" is a modulo sign)
C=A%B                       # The denominator is positive, so remainder is positive 
print(C)


A,B=5,-2
C=A%B                       # The denominator is negative, so remainder is negative. 
print(C)

A,B=-5,-2
C=A%B                       # The denominator is negative, so the remainder is also negative.
print(C)

A,B=2,3
C=4                      # Numeric values can operates with all the arithmetic operators.
print(A+B*C)

A,B=10,5.0
C=A*B                    # Arithmetic expression with integers and float will result in float.
print(C)

# Relational operators :-

a = 50
b = 20

print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)


# Assignment operators :- 

num = 10
num += 10               # num += 10 & num = num + 10 , Both are same. 
print("num : ", num)

#  Similarly, other assignment operators works as above.


## Logical operators :-  [not,and,or]

print(not True)
print(not False)

a = 50
b = 30 
print(not(a>b))

val1 = True
val2 = False
print("And operator:", val1 and val2)
print("Or operator:", val1 or val2)

print("Or operator:", (a == b) or (a > b))
