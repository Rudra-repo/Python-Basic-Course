# QUE: WAP using functions to find greatest of three numbers.


# def greatest(a,b,c):
#     if(a>b and a>c):
#         print("a is greatest")
#     elif(b>a and b>c):
#         print("b is greatest")
#     elif(c>a and c>b):
#         print("c is greatest")

# greatest(23,12,34)

# QUE: WAP using function to convert celsius to fahrenheit.

# def temp_convert(celsius):
#     fahrenheit = (celsius*1.8)+32
#     return fahrenheit


# print(temp_convert(34))

#  QUE: How do you prevent a python print() function to print a new line at the end.

# print("what are you doing?",end="")                 # By using end="" as it prevents to move to next line.
# print()

# QUE: Write a recursive function to calculate the sum of first n natural numbers.

# def show(n):
#     if(n == 0):
#         return 0
#     return show(n-1)+n

# sum = show(5)
# print(sum)

# QUE: Write a python function to print first n lines of the following pattern:

'''
***
**                  for n=3
*
'''

# def pattern(n):
#     if(n == 0):
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(5)

# QUE: Write a python function which converts inches to cms.

# def inch_to_cm(inch):
#     return 2.54*(inch)

# inch = int(input("Enter the length in inch: "))
# print(f"{inch_to_cm(inch)}cm")

# QUE: Write a python function to remove a given word from list and strip it at the same time.

# def remove(list,word):
#     for item in list:
#         list.remove(word)
#         return list

# list = ["Ram","Rohan","rudra","an"]

# print(remove(list,"an"))

# def remove(list,word):
#     n = []
#     for item in list:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# list = ["Ram","Rohan","rudra","an"]

# print(remove(list,"an"))

# QUE: Write a python function to print multiplication table of given number.

def table():
    n = int(input("Enter the number: "))

    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    return

print(table())