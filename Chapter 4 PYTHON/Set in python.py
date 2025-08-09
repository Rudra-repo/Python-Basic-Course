# Set is the collection of the unordered items.                            # IMP NOTE :- [Hence, Sets are mutable.]
# Each element in the set must be unique & immutable.                       Sets are mutable but the elements are immutable , we cannot change the value of element but can add or remove the value from the set 


nums = {1,2,3,4}
set2 = {1,2,2,2}
# repeated elements stored only once, so it resolved to {1,2}

null_set = set()            # empty set syntax

collection = {1,2,2,2,"hello","world","world",4}

print(collection)
print(type(collection))
print(len(collection))

collection = {}             # this is syntax for empty dictionary
print(type(collection))

# If we need to create empty set, this following syntax is used

collection = set()
print(type(collection))


# SET METHODS :- 
# set.add(el)       # adds an element
# set.remove(el)    # removes the element
# set.clear()       # empties the set
# set.pop()         # removes a random value
# set.union( set2 ) # combines both set values & returns new 
# set.intersection( set2 )  # combines common values and returns new.

collection = set()
collection.add(1)               # we can add any immutable function like string,int,float,tuple, etc but not 'list' as it is mutable
collection.add(2)
collection.add(2)
collection.add("Rudra")
collection.add((1,2,3))

collection.remove(1)
collection.clear()

print(collection)
print(len(collection))

collection = {"hello", "scaler", "world", "coding", "python"}

print(collection.pop())
print(collection.pop())

# UNION & INTERSECTION OF SET :

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))

collection = {34, 32, 78, 65, 65, 2 }
collection.add(1)
print(collection)