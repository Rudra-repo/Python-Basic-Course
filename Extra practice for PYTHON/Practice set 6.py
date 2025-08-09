# QUE: WAP to find the greatest of four numbers entered by the user.

a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
c = int(input("Enter 3rd no.: "))
d = int(input("Enter 4th no.: "))

if(a>b and a>c and a>d):
    print("a is the greatest of all")
elif(b>a and b>c and b>d):
    print("b is the greatest of all")
elif(c>a and c>b and c>d):
    print("c is the greatest of all.")
else:
    print("d is the greatest of all")
    

# QUE: WAP to find out whether a student has passed or failed if it required a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
name = input("Enter your name: ")
marks1 = int(input("Enter marks of 1st subject: "))
marks2 = int(input("Enter marks of 2nd subject: "))
marks3 = int(input("Enter marks of 3rd subject: "))

Total_percentage = (marks1+marks2+marks3)/3

if(marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and Total_percentage >= 40):
    print("Congratulations!!!", name, "\n You passed this session.")
else:
    print("Sorry",name,"\nTry your luck next time.")

# QUE: A spam comment is defined as a text containing following keywords:
# "Make a lot of money","buy now","subscribe this","click this". WAP to detect these spams.

a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

message = input("Enter your message: ")

if(a in message or b in message or c in message or d in message):
    print("Spam comments are there.")
else:
    print("No spam comment are there, you can fluently read this without any hindrence.")

# QUE: WAP to find out whether a given username contains less than 10 characters or not.

user_name = input("Enter username : ")

if(len(user_name) < 10):
    print("username contains less than 10 characters.")
else:
    print("username contains more than or equal to 10 characters.") # this also includes spaces between the words

# QUE: WAP which finds out whether a given name is present in a list or not.

list = ["Rudra","Mohan","Satyam","Jagtar","Harsh"]

name = input("Enter your name : ")

if(name in list):
    print("Your name is in the list.")
else:
    print("Your name is not in the list.")

# QUE: WAP to find out whether a given post is talking about "Rudra" or not.

post = input("Enter the post : ")
name = "Rudra"

if(name in post ):
    print("This post talking about Rudra.")
else:
    print("This post is not talking about Rudra.")