# DICTIONARY in Python :-

# They are unordered, mutable(changeable) & don't allow duplicate keys 
# Dictionary works in pair like [WORD -> MEANING] . Generally, words acts as a key as we write word to find it's meaning.

dict = {
    "name" : "Rudra",
    "cgpa" : 9.4,
    "marks" : [93,94,95],
    "age" : 19,
    "is_adult" : True,
}

print(dict["name"], dict["cgpa"], dict["marks"])

info = {
    "key" : "value",
    "college" : "Scaler",                    # In 'keys' lists and dictionary is not acceptable whereas 'value' can store any of datatype.
    "learning" : "coding",
    "marks" : 94.4,                         # whereas 'keys' can even store int, float values,even tuple [Basically, Non-mutable values could be assigned to 'keys'].
    "age" : 19,
    "is_adult" : True,
    "subjects" : ["Python", "C", "Java"],
    "topics" : ("dict", "set"),
}
print(type(info))
print(info)

info["college"] = "IIT Madras"          # Rather, assigning new value to the 'key' dictionary overwrite the new value of that key.
info["key"] = "House key"
info["age"] = 76

print(info)

null_dict = {}
null_dict["name"] = "Rudra"
print(null_dict)


# NESTED DICTIONARY :-

student = {
    "name" : "Rudra",
    "score" : {
        "chem" : 89,
        "phy" : 94,
        "maths" : 92,
    }
}
print(student)

print(student["score"]["chem"])

