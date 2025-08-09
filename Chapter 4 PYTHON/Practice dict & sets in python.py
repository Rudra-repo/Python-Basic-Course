# QUE: Store following word meaning in aa python dictionary :
        # table : "a piece of furniture", "list of facts & figures"
        # cat : "a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
}

print(dictionary)


# QUE: You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroom are needed by all students.
        # "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"

subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# If one classroom is required for 1 subject so set of subject = no. of classroom is required

print(subjects)
print(len(subjects))


# QUE: WAP to enter marks of 3 subjects from the user and store then in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter maths : "))
marks.update({"maths" : x})

print(marks)


# QUE: Figure out a way to store 9 and 9.0 as separate values in the set.(Hint:You can take help of built-in data types)

values = {9,"9.0"}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)     
}
print(values)