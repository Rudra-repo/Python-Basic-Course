# "FOR" LOOPS IN PYTHON:

# Loops are used for sequential traversal. For traversing list, string, tuples etc.

# FOR LOOPS :-
# For el in list: 
        # some work 


list = [1,2,3]
for el in list:
    print(el)
print("End")

# For loop with else 
# for el in list:
        # some work
# else:
        # work when loop ends 


for el in list:
    print(el)
else:
    print("End")


nums = [1,2,3,4,5]

for val in nums:
    print(val)
print("end")


vaggies = ["potato", "Brinjal", "ladyfinger", "cucumber"]

for val in vaggies:
    print(val)
print("End of code")


tup = (1,4,6,8,9,7)

for num in tup:
    print(num)

print("The Emd")


str = "Rudra Pratap Singh"

for char in str:
    print(char)
print("End of loop")


# Both of them give same output but "else" is used in some cases like while we are using 'Break'.
str = "Rudra Pratap Singh"

for char in str:
    if( char == "S"):
        print("S found")
        break
    print(char)
else:
    print("End")