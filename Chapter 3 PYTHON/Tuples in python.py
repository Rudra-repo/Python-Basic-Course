# TUPLES IN PYTHON :- 
# A built-in data type that lets us create immutable sequences of values.

tup = (87, 64, 33, 95, 76)          # tup[0], tup[1]...

# tup[0] = 43                         # NOT allowed in python

tup1 = ()
tup2 = (1,)                     # This is right way to write single valued tuple as (1) is considered as int value. [ Put 'Comma' after entering the only single value]
tup3 = (1,2,3)                  # We can use comma or not depending on us for more than single valued tuple as considered to be right.

print(tup1,tup2,tup3)

print(tup2[0])

print(type(tup1))

print(tup3[2])



# TUPLE METHODS :- 

tup = (2,1,3,1)

# tup.index(el)             # returns index of first occurence      #tup.index(1) is 1

print(tup.index(3))

# tup.count(el)            # counts total occurences              # tup.count(1) is 2

print(tup.count(1))


tup = (23,23,24,24,24,36,24,37,65,97,27)                # if values are repeated in tuple then it will give smaller index of the particular value.

print(tup.index(97))
print(tup.count(24))

