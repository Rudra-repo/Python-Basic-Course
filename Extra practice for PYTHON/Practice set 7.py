# QUE: WAP to print multiplication table of a given number using for loop.

n = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
else:
    print("done")

# QUE: WAP to greet all the person names stored in a list 'l' and which starts with S.

l = ["Harry","Soham","Sachin","Rahul"]

for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")

# # QUE: Attempt problem 1 using while loop.

n = int(input("Enter the no.: ")) 

i = 1
while i<=10:
    print(f"{n} X {i} = {n*i}")
    i += 1
else:
     print("Done")

# QUE: WAP to find whether a given no. is prime or not.

n = int(input("Enter the no.: "))

for i in range(2,n):
    if(n%i == 0):
        print(f"{n} is not a prime no.")
        break
else:
        print(f"{n} is a prime no.")

# # QUE: WAP to find the sum of first n natural numbers using while loop.

n = int(input("Enter the no.: "))

sum = 0
i = 1
while i <= n :
    
     i += 1
     sum += i

print(sum)

# # QUE: WAP to calculate the factorial of a given number using for loop.

n = int(input("Enter your no.: "))

product = 1
for i in range(1,n+1):
     product *= i

print(f"factorial  of {n} is {product}")

# # QUE: WAP to print the following pattern.
'''

for n = 3
  *
 ***
*****        for (n = 3)

'''

n = int(input("Enter the no.: "))

for i in range(1,n+1):
     
    print(" " * (n-i),end="")
    print("* " * (2*i-1), end="")
    print("")

# QUE: WAP to print the following star pattern:
'''
*
**
***
'''

n = int(input("Enter the no.: "))

for i in range(1,n+1):
    print("*" * i,end ="")
    print("")

# QUE: WAP to print the following star pattern.
'''
***
* *
***
'''
n = int(input("Enter the no.: "))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")

