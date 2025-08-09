# PASS STATEMENT :-
# pass is a null statement that does nothing. It is used as a placeholder for future code.

for el in range(10):
    pass                    # Empty

print("some useful work")

# LET'S PRATICE :-

# QUE: WAP to find the sum of first n natural numbers. (using while)

n = int(input("enter no.: "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(" total sum =", sum)

#  this is done by for loop method:
sum = 0
for el in range(1,n+1):
    sum += el

print(" total sum =", sum)


# QUE: WAP to find the factorial of first n numbers. (using for)

n = int(input("enter no.: "))

product = 1
for i in range(1,n+1):
    product *= i
print("Factorial of n =", product)