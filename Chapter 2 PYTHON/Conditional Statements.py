# Conditional Statements :-
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

print("End of code")


# Voting Code

age = int(input("age : "))

if(age >= 18):
    print("Can VOTE")           # Indentation :- it is the proper spacing while writing code, here tab space is used.
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

print("marks of the student ->", marks)


# NESTING :- 

age = int(input("age: "))

if(age >= 18):
    if(age >= 80):
        print("cannot drive")               # Nesting [Condition ke andar ek aur condition]
    print("can drive")
else:
    print("cannot drive")

print("End of code")

