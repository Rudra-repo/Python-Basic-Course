# RANGE () :-
# Range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# range(starts?, stop, step?)
 
seq = range(10)         # 10 is a stopping condition

for i in seq:                   # Generally, last number is not included.
    print(i)

print(range(5))

for i in range(2, 8):           # here, we provided both the conditions (starting, ending)
    print(i)

for i in range(2, 8,3):           # here, we provided all the required conditions (starting, ending, step), only those no printed who fulfilled all the condition nono other no printed
    print(i)

# printing even number via using range method :-

for i in range(2,10,2):
    print(i)

print("End of code")

# LET'S PRACTICE [USING FOR AND RANGE()]:-

# Print numbers from 1 to 100.

for i in range(1,101):
    print(i)

print("End")

# Print numbers from 100 to 1.

for i in range(100,0,-1):
    print(i)

print("Loop is ended")

# print the multiplication rable of a number n.

for i in range(6,66,6):         # this is the worst method
    print(i)

print("Ended")

#  this is the best method:
 
n = int(input("Enter no.: "))

for i in range(1,11):
    print(i*n)

print("End")