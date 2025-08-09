# QUE: WAP to display a user entered name followed by Good Afternoon using input() function.

name = input("Enter your name: ")
print("Good Afternoon", name,"!!")

# NEW METHOD Via 'f' string:-
print(f"Good Afternoon {name} ")

# QUE: WAP to fill in a letter template given below with name and date.
letter = '''
Dear <|name|>,
You are selected
<|Date|>
'''
name = input("Enter your name: ")
Date = input("Enter the date: ")

print("Dear",name,",\nYou are selected\n", Date)
#               OR
print(letter.replace("<|name|>","Rudra").replace("<|Date|>","17|07|2025"))
# print(letter.replace("<|Date|>","17|07|2025"))            # Here, this will give stated  mistakes as we run two commands on two different times, thus we get two different undesired wrong result.

# QUE: WAP to detect double space in a string.

name = "Rudra might  be there for your help."

print(name.find("  "))
# if double space is not there then it will give -1 as a result.

# QUE: Replace the double space from problem 3 with single spaces.

print(name.replace("  "," "))

# QUE: WAP to format the following letter using escape sequence characters.
# letter = "Dear Rudra, this python course is nice. Thanks!"

letter = "Dear Rudra,\nthis python course is nice.\nThanks!"
print(letter)