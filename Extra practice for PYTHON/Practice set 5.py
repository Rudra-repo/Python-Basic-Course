# QUE: WAP to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

Dict = {
    "Ghar" : "House",
    "Kitab" : "Book",
    "Aankh" : "Eye",
    "Kela" : "Banana",
    "Lal" : "Red"
}
word = input("Enter the word : ")

print(Dict[word])

# QUE: WAP to input eight numbers from the user and display all the unique numbers(once)

s = set()
n = input("Enter no. 1 : ")
s.add(int(n))
n = input("Enter no. 2 : ")
s.add(int(n))
n = input("Enter no. 3 : ")
s.add(int(n))
n = input("Enter no. 4 : ")
s.add(int(n))
n = input("Enter no. 5 : ")
s.add(int(n))
n = input("Enter no. 6 : ")
s.add(int(n))
n = input("Enter no. 7 : ")
s.add(int(n))
n = input("Enter no. 8 : ")
s.add(int(n))

print(s)

# QUE: Can we have a set with '18' (str) as value in it?

s = {2,4,5,6,"18",18,34,56}

print(s) # yes, it is possible
#           OR
s = set()
s.add(18)
s.add("18")

print(s)

# QUE: What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)    # 20.0 and 20 is considered as same in python that's why lenght is 2.
s.add("20")

print(s)
print(len(s))

# QUE: What is the type of S = {}

S = {}
print(type(S))  # It is dict type.

# QUE: Create an empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.

dict = {}

fav_lang = input("Enter favourite lang. : ")
dict.update({"Rohan" : fav_lang})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Rudra" : fav_lang})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Mohan" : fav_lang})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Satyam" : fav_lang})

print(dict)

# QUE: If the names of 2 friends are same; what will happen to the programme in last problem.

dict = {}

fav_lang = input("Enter favourite lang. : ")
dict.update({"Rohan" : fav_lang})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Rudra" : fav_lang})
fav_lang1 = input("Enter favourite lang. : ")       # As the dict is 2nd time updated so recent update is in consideration, other will wiped off.
dict.update({"Rudra" : fav_lang1})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Satyam" : fav_lang})

print(dict)

# QUE: If the names of 2 Subjects are same; what will happen to the programme in last problem.

dict = {}

fav_lang = input("Enter favourite lang. : ")
dict.update({"Rohan" : fav_lang})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Rudra" : fav_lang})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Mohan" : fav_lang})
fav_lang = input("Enter favourite lang. : ")
dict.update({"Satyam" : fav_lang})

print(dict)         # Nothing will change as value can be duplicate but keys aren't.

# QUE: Can you change the values inside a list which is contained in set S ?

# S = {8,7,12,"Rudra",[1,2]}      # Lists cannot be a part of set as they are mutable but in set we only required immutable values.

# print(S)

# So, this cannot be change even the list cannot be a part of set, as sets are immutable.

