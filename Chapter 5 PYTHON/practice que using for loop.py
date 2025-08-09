# QUE: Print the elements of the following list using a loop :
        # [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

for val in nums:
    print(val)
print("The End")


# QUE: Search for a number x in this tuple using loop:

x = 89
for val in nums:
    if(val == 89):
        print("x is found")
        break
    print(val)

else:
    print("not found")


# For finding at which idx the element is :-
x = 49

idx = 0
for el in nums:
    if(el == x):                                # if you have repeated elements in list & you want to print idx of both of them then don't use break function and rest is same
        print("number found at idx", idx)
        break
    idx += 1