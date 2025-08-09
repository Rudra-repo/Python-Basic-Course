# if-elif-else (SYNTAX)

# Traffic Light Code 

light = input("light : ")
if(light == "red"):
    print("STOP")
elif(light == "green"):
    print("GO")
elif(light == "yellow"):
    print("WAIT")
else:
    print("light is Broken")


# Voting Code

age = int(input("age : "))
if(age >= 18):
    print("Can VOTE")
else:
    print("Can't VOTE")


# Grades of Students

marks = int(input("marks : "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")

# Single line IF / Ternary operators 

food = input("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

# Clever If / Ternary operators :- 

age = int(input("age : "))
vote = ("yes","no") [age>=18]

sal = float(input("salary : "))
tax = sal*(0.1,0.2) [sal<=50000]
print(tax)

