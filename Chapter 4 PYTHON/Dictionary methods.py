# Dictionary Methods :-

# myDict.keys()         # return all keys
# myDict.values()       # return all values
# myDict.items()        # returns all (keys, values) pairs as tuples
# myDict.get("key")     # returns the key according to value
# myDict.update(new Dict) # inserts the specified items to the dictionary

student = {
    "name" : "Rudra",
    "score" : {
        "chem" : 89,
        "phy" : 94,
        "maths" : 92,
    }
}

print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])

print(student.get("score"))

print(list(student.get("name")))

print(student["name"])              # if we enter name2 instead of name in this function it will give an ERROR
print(type(student["name"]))


print(student.get("name"))          # Whereas, here it does not give error instead error it give us 'NONE'

new_dict = {"city" : "bhind"}
student.update(new_dict)

print(student)